from typing import Optional, Any

import ujson
from aiohttp import ClientSession, ClientResponse, StreamReader

from app.utils import Singleton


class AiohttpClient:

    def __init__(
            self,
            session: Optional[ClientSession] = None,
            **session_params: dict
    ) -> None:
        self.session = session
        self._session_params = session_params

    async def request_raw(self, url: str, method: str = "GET", data: Optional[dict] = None, **kwargs) -> ClientResponse:
        if not self.session:
            self.session = ClientSession(
                json_serialize=ujson.dumps,
                **self._session_params
            )

        async with self.session.request(url=url, method=method, data=data, **kwargs) as response:
            await response.read()
            return response

    async def request_text(self, url: str, method: str = "GET", data: Optional[dict] = None, **kwargs) -> str:
        response = await self.request_raw(url, method, data, **kwargs)
        return await response.text()

    async def request_json(self, url: str, method: str = "GET", data: Optional[dict] = None, **kwargs) -> dict:
        response = await self.request_raw(url, method, data, **kwargs)
        return await response.json(
            encoding='utf-8',
            loads=ujson.loads,
            content_type=None
        )

    async def request_content(
            self, url: str, method: str = "GET", data: Optional[dict] = None, **kwargs
    ) -> StreamReader:
        response = await self.request_raw(url, method, data, **kwargs)
        return response.content

    async def close(self) -> None:
        if self.session and not self.session.closed:
            await self.session.close()


class SingleAiohttpClient(AiohttpClient, metaclass=Singleton):
    ...
