"""Pagination classes for tap-everflow."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import TYPE_CHECKING

from singer_sdk.pagination import BaseAPIPaginator
from typing_extensions import override

if TYPE_CHECKING:
    from tap_everflow.streams import ClicksStream


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
