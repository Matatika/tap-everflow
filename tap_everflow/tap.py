"""Everflow tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers
from typing_extensions import override

from tap_everflow import streams


class TapEverflow(Tap):
    """Everflow tap class."""

    name = "tap-everflow"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            secret=True,
            title="API Key",
            description="Everflow network API key",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync",
        ),
    ).to_dict()

    @override
    def discover_streams(self):
        return [
            streams.OffersStream(self),
            streams.ConversionsStream(self),
        ]


if __name__ == "__main__":
    TapEverflow.cli()
