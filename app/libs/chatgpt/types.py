from datetime import datetime
from dataclasses import dataclass


@dataclass
class Usage:
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


@dataclass
class Message:
    role: str
    content: str


@dataclass
class Choice:
    index: int
    message: Message
    finish_reason: str


@dataclass
class GPTResponse:
    id: str
    object: str
    created: datetime
    model: str
    choices: list
    usage: Usage
    system_fingerprint: str


@dataclass
class GPTError:
    type: str
    message: str
