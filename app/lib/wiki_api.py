from typing import TYPE_CHECKING
from dataclasses import dataclass

import ujson

from app.lib.http import AiohttpClient


@dataclass
class WikiArticleResponse:
    title: str
    summary: str
    article_url: str


class WikiAPI:

    BASE_API_URI = 'https://ru.wikipedia.org/api/rest_v1/page/summary/'

    def __init__(self) -> None:
        self.http = AiohttpClient()

    async def get_article(self, response: str) -> WikiArticleResponse | None:
        response = await self.http.request_raw(self.BASE_API_URI + response)

        if response.status != 200:
            return

        response_json = await response.json(
            encoding='utf-8',
            loads=ujson.loads,
            content_type=None
        )
        return WikiArticleResponse(
            title=response_json['title'],
            summary=response_json['extract'],
            article_url=response_json['content_urls']['desktop']['page']
        )
