import logging
from datetime import datetime

from .abc import ABCChatGptAPI
from .types import (
    GPTError,
    GPTResponse,
    Choice,
    Message,
    Usage
)
from app.lib.http import AiohttpClient


class NagaChatGptAPI(ABCChatGptAPI):

    BASE_URL = 'https://api.naga.ac/v1/chat/completions'

    def __init__(self, model: str, token: str, start_context: str) -> None:
        self.__headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }
        self.__model = model
        self.__start_context = start_context

        self.__http = AiohttpClient()

    async def make_request(self, prompt: str) -> GPTResponse | GPTError:
        payload = {
            'model': self.__model,
            'messages': [
                {
                    'role': 'system',
                    'content': self.__start_context
                },
                {
                    'role': 'user',
                    'content': prompt
                }
            ]
        }

        logging.debug(f'GTP PAYLOAD: {payload}')

        response = await self.__http.request_json(
            url=self.BASE_URL,
            method='POST',
            json=payload,
            headers=self.__headers
        )

        logging.debug(f"GPT RESPONSE: {response}")

        if 'error' in response:
            error = response['error']
            return GPTError(
                type=error.get('type'),
                message=error.get('message')
            )

        return GPTResponse(
            id=response['id'],
            object=response['object'],
            created=datetime.fromtimestamp(response['created']),
            model=response['model'],
            choices=[
                Choice(
                    index=choice['index'],
                    message=Message(
                        role=choice['message']['role'],
                        content=choice['message']['content']
                    ),
                    finish_reason=choice['finish_reason']
                ) for choice in response['choices']
            ],
            usage=Usage(
                prompt_tokens=response['usage']['prompt_tokens'],
                completion_tokens=response['usage']['completion_tokens'],
                total_tokens=response['usage']['total_tokens']
            ),
            system_fingerprint=response.get('system_fingerprint')
        )
