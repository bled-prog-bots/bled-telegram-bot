from abc import ABC, abstractmethod

from .types import GPTResponse, GPTError


class ABCChatGptAPI(ABC):

    @abstractmethod
    def __init__(self) -> None:
        ...

    @abstractmethod
    def make_request(self, question: str) -> GPTResponse | GPTError:
        ...
