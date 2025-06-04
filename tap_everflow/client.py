"""REST client handling, including EverflowStream base class."""

from __future__ import annotations

from datetime import timezone
from functools import cached_property

from singer_sdk.authenticators import APIKeyAuthenticator
from singer_sdk.streams import RESTStream
from typing_extensions import override

from tap_everflow.pagination import EverflowPaginator


class EverflowStream(RESTStream):
    """Everflow stream class."""

    url_base = "https://api.eflow.team/v1"

    @override
    @cached_property
    def authenticator(self):
        return APIKeyAuthenticator.create_for_stream(
            self,
            key="X-Eflow-API-Key",
            value=self.config.get("api_key", ""),
            location="header",
        )

    @override
    def get_new_paginator(self):
        return EverflowPaginator()

    @override
    def get_url_params(self, context, next_page_token):
        params = {}

        if next_page_token:
            params["page"] = next_page_token

        params["page_size"] = 2000

        return params

    @cached_property
    def utc_timezone_id(self):
        """Resolve UTC timezone ID from API."""
        response = self.requests_session.get(f"{self.url_base}/meta/timezones")
        response.raise_for_status()
        timezones: list[dict] = response.json()["timezones"]

        for tz in timezones:
            if tz["timezone"] == str(timezone.utc):
                return tz["timezone_id"]

        msg = "No UTC timezone found"
        raise RuntimeError(msg)
