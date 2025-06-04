"""Pagination classes for tap-everflow."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import TYPE_CHECKING

from singer_sdk.pagination import BaseAPIPaginator
from typing_extensions import override

if TYPE_CHECKING:
    from tap_everflow.streams import ClicksStream


class EverflowPaginator(BaseAPIPaginator):
    """Everflow paginator."""

    @override
    def __init__(self) -> None:
        super().__init__(None)

    @override
    def has_more(self, response):
        paging = response.json()["paging"]

        page: int = paging["page"]
        page_size: int = paging["page_size"]
        total_size: int = paging["total_count"]

        return page_size * page < total_size

    @override
    def get_next(self, response):
        paging = response.json()["paging"]
        return paging["page"] + 1


class ClicksPaginator(BaseAPIPaginator):
    """Clicks paginator."""

    @override
    def __init__(self, stream: ClicksStream) -> None:
        super().__init__(None)
        self.stream = stream

    @override
    def get_next(self, response):
        next_value: int = response.json()["clicks"][0][self.stream.replication_key]
        next_date = datetime.fromtimestamp(next_value, tz=timezone.utc)

        if (
            next_date.strftime(r"%Y-%m-%d %H:%M:%S")
            == json.loads(response.request.body)["from"]
        ):  # if next date is equal to the last requested from date
            return None  # end pagination

        return next_date
