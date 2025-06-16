"""Stream type classes for tap-everflow."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from functools import cached_property

from singer_sdk import typing as th
from typing_extensions import override

from tap_everflow import schemas
from tap_everflow.client import EverflowStream
from tap_everflow.pagination import ClicksPaginator


class OffersStream(EverflowStream):
    """Define offers stream."""

    name = "offers"
    primary_keys = ("network_offer_id",)
    path = "/networks/offers"
    records_jsonpath = "$.offers[*]"

    @override
    @cached_property
    def schema(self):
        return th.PropertiesList(
            th.Property("network_offer_id", th.IntegerType),
            th.Property("network_id", th.IntegerType),
            th.Property("network_advertiser_id", th.IntegerType),
            th.Property("network_offer_group_id", th.IntegerType),
            th.Property("name", th.StringType),
            th.Property("thumbnail_url", th.StringType),
            th.Property("network_category_id", th.IntegerType),
            th.Property("internal_notes", th.StringType),
            th.Property("destination_url", th.StringType),
            th.Property("server_side_url", th.StringType),
            th.Property("is_view_through_enabled", th.BooleanType),
            th.Property("view_through_destination_url", th.StringType),
            th.Property("preview_url", th.StringType),
            th.Property("offer_status", th.StringType),  # active, deleted
            th.Property("currency_id", th.StringType),
            th.Property("caps_timezone_id", th.IntegerType),
            th.Property("project_id", th.StringType),
            th.Property("date_live_until", th.DateType),
            th.Property("html_description", th.StringType),
            th.Property("is_using_explicit_terms_and_conditions", th.BooleanType),
            th.Property("terms_and_conditions", th.StringType),
            th.Property("is_force_terms_and_conditions", th.BooleanType),
            th.Property("is_caps_enabled", th.BooleanType),
            th.Property("daily_conversion_cap", th.IntegerType),
            th.Property("weekly_conversion_cap", th.IntegerType),
            th.Property("monthly_conversion_cap", th.IntegerType),
            th.Property("global_conversion_cap", th.IntegerType),
            th.Property("daily_payout_cap", th.IntegerType),
            th.Property("weekly_payout_cap", th.IntegerType),
            th.Property("monthly_payout_cap", th.IntegerType),
            th.Property("global_payout_cap", th.IntegerType),
            th.Property("daily_revenue_cap", th.IntegerType),
            th.Property("weekly_revenue_cap", th.IntegerType),
            th.Property("monthly_revenue_cap", th.IntegerType),
            th.Property("global_revenue_cap", th.IntegerType),
            th.Property("daily_click_cap", th.IntegerType),
            th.Property("weekly_click_cap", th.IntegerType),
            th.Property("monthly_click_cap", th.IntegerType),
            th.Property("global_click_cap", th.IntegerType),
            th.Property("redirect_mode", th.StringType),  # standard
            th.Property("is_using_suppression_list", th.BooleanType),
            th.Property("suppression_list_id", th.IntegerType),
            th.Property("is_must_approve_conversion", th.BooleanType),
            th.Property("is_allow_duplicate_conversion", th.BooleanType),
            th.Property("is_duplicate_filter_enabled", th.BooleanType),
            th.Property("duplicate_filter_targeting_action", th.StringType),  # unknown
            th.Property("network_tracking_domain_id", th.IntegerType),
            th.Property("is_use_secure_link", th.BooleanType),
            th.Property("is_seo_friendly", th.BooleanType),
            th.Property("is_allow_deep_link", th.BooleanType),
            th.Property("is_session_tracking_enabled", th.BooleanType),
            th.Property(
                "session_tracking_start_on",
                th.StringType,
            ),  # click, null_value
            th.Property("session_tracking_lifespan_hour", th.IntegerType),
            th.Property("session_tracking_minimum_lifespan_second", th.IntegerType),
            th.Property("is_view_through_session_tracking_enabled", th.BooleanType),
            th.Property(
                "view_through_session_tracking_lifespan_minute",
                th.IntegerType,
            ),
            th.Property(
                "view_through_session_tracking_minimal_lifespan_second",
                th.IntegerType,
            ),
            th.Property("is_block_already_converted", th.BooleanType),
            th.Property("already_converted_action", th.StringType),  # unknown
            th.Property("is_fail_traffic_enabled", th.BooleanType),
            th.Property(
                "redirect_routing_method",
                th.StringType,
            ),  # internal, null_value
            th.Property(
                "redirect_internal_routing_type",
                th.StringType,
            ),  # null_value, priority
            th.Property("visibility", th.StringType),  # private
            th.Property("time_created", th.IntegerType),
            th.Property("time_saved", th.IntegerType),
            th.Property(
                "conversion_method",
                th.StringType,
            ),  # html_pixel_cookie_based, javascript, server_postback
            th.Property("is_whitelist_check_enabled", th.BooleanType),
            th.Property("is_use_scrub_rate", th.BooleanType),
            th.Property("scrub_rate_status", th.StringType),  # null_value, rejected
            th.Property("scrub_rate_percentage", th.IntegerType),
            th.Property("session_definition", th.StringType),  # cookie, ip_user_agent
            th.Property("session_duration", th.IntegerType),
            th.Property("app_identifier", th.StringType),
            th.Property("is_description_plain_text", th.BooleanType),
            th.Property("is_use_direct_linking", th.BooleanType),
            th.Property(
                "relationship",
                th.ObjectType(
                    th.Property(
                        "category",
                        th.ObjectType(
                            th.Property("network_category_id", th.IntegerType),
                            th.Property("network_id", th.IntegerType),
                            th.Property("name", th.StringType),
                            th.Property("status", th.StringType),  # active
                            th.Property("time_created", th.IntegerType),
                            th.Property("time_saved", th.IntegerType),
                        ),
                    ),
                    th.Property(
                        "labels",
                        th.ObjectType(
                            th.Property("total", th.IntegerType),
                            th.Property("entries", th.ArrayType(th.StringType)),
                        ),
                    ),
                    th.Property(
                        "payout_revenue",
                        th.ObjectType(
                            th.Property("total", th.IntegerType),
                            th.Property(
                                "entries",
                                th.ArrayType(
                                    th.ObjectType(
                                        th.Property(
                                            "network_offer_payout_revenue_id",
                                            th.IntegerType,
                                        ),
                                        th.Property("network_id", th.IntegerType),
                                        th.Property("network_offer_id", th.IntegerType),
                                        th.Property("entry_name", th.StringType),
                                        th.Property(
                                            "payout_type",
                                            th.StringType,
                                        ),  # cpa, cpc
                                        th.Property("payout_amount", th.NumberType),
                                        th.Property(
                                            "payout_percentage", th.IntegerType
                                        ),
                                        th.Property(
                                            "revenue_type",
                                            th.StringType,
                                        ),  # rpa, rpc
                                        th.Property("revenue_amount", th.NumberType),
                                        th.Property(
                                            "revenue_percentage", th.IntegerType
                                        ),
                                        th.Property("is_default", th.BooleanType),
                                        th.Property("is_private", th.BooleanType),
                                        th.Property(
                                            "is_postback_disabled", th.BooleanType
                                        ),
                                        th.Property("is_enforce_caps", th.BooleanType),
                                        th.Property("time_created", th.IntegerType),
                                        th.Property(
                                            "global_advertiser_event_id",
                                            th.IntegerType,
                                        ),
                                        th.Property(
                                            "is_must_approve_conversion",
                                            th.BooleanType,
                                        ),
                                        th.Property(
                                            "is_allow_duplicate_conversion",
                                            th.BooleanType,
                                        ),
                                        th.Property(
                                            "is_email_attribution_default_event",
                                            th.BooleanType,
                                        ),
                                        th.Property(
                                            "remote_offer_resource",
                                            th.ObjectType(
                                                th.Property(
                                                    "network_offer_id",
                                                    th.IntegerType,
                                                ),
                                                th.Property(
                                                    "network_id", th.IntegerType
                                                ),
                                                th.Property(
                                                    "resource_type", th.StringType
                                                ),
                                                th.Property(
                                                    "remote_resource_id",
                                                    th.StringType,
                                                ),
                                                th.Property(
                                                    "resource_id", th.IntegerType
                                                ),
                                                th.Property(
                                                    "last_value_md5",
                                                    th.StringType,
                                                ),
                                                th.Property(
                                                    "json_config", th.StringType
                                                ),
                                                th.Property("json_data", th.StringType),
                                                th.Property(
                                                    "time_created", th.IntegerType
                                                ),
                                                th.Property(
                                                    "time_saved", th.IntegerType
                                                ),
                                            ),
                                        ),
                                    )
                                ),
                            ),
                        ),
                    ),
                    th.Property("encoded_value", th.StringType),
                    th.Property("is_locked_currency", th.BooleanType),
                    th.Property("channels", th.ArrayType(th.AnyType)),
                    th.Property(
                        "channels",
                        th.ObjectType(
                            th.Property("total", th.IntegerType),
                            th.Property("entries", th.ArrayType(th.AnyType)),
                        ),
                    ),
                    th.Property("is_locked_caps_timezone", th.BooleanType),
                    th.Property("meta", th.ObjectType(additional_properties=True)),
                    th.Property(
                        "requirement_kpis",
                        th.ObjectType(
                            th.Property("total", th.IntegerType),
                            th.Property("entries", th.ArrayType(th.AnyType)),
                        ),
                    ),
                    th.Property(
                        "requirement_tracking_parameters",
                        th.ObjectType(
                            th.Property("total", th.IntegerType),
                            th.Property("entries", th.ArrayType(th.AnyType)),
                        ),
                    ),
                ),
            ),
            th.Property("is_email_attribution_enabled", th.BooleanType),
            th.Property(
                "email_attribution_method",
                th.StringType,
            ),  # first_affiliate_attribution, unknown
            th.Property("attribution_method", th.StringType),  # last_touch
            th.Property("is_email_attribution_window_enabled", th.BooleanType),
            th.Property("email_attribution_window_minute", th.IntegerType),
            th.Property("email_attribution_window_type", th.StringType),  # unknown
            th.Property("is_soft_cap", th.BooleanType),
        ).to_dict()

    @override
    def post_process(self, row, context=None):
        if not row.get("date_live_until"):
            row["date_live_until"] = None

        return row


class ConversionsStream(EverflowStream):
    """Define conversions stream."""

    name = "conversions"
    primary_keys = ("conversion_id",)
    replication_key = "conversion_unix_timestamp"
    http_method = "POST"
    path = "/networks/reporting/conversions"
    records_jsonpath = "$.conversions[*]"

    @override
    @cached_property
    def schema(self):
        return th.PropertiesList(
            th.Property("conversion_id", th.StringType),
            th.Property("conversion_unix_timestamp", th.IntegerType),
            th.Property("sub1", th.StringType),
            th.Property("sub2", th.StringType),
            th.Property("sub3", th.StringType),
            th.Property("sub4", th.StringType),
            th.Property("sub5", th.StringType),
            th.Property("source_id", th.StringType),
            th.Property("status", th.StringType),  # approved, pending
            th.Property("payout_type", th.StringType),  # cpa
            th.Property("revenue_type", th.StringType),  # rpa
            th.Property("payout", th.IntegerType),
            th.Property("revenue", th.IntegerType),
            th.Property("session_user_ip", th.StringType),
            th.Property("conversion_user_ip", th.StringType),
            th.Property("country", th.StringType),
            th.Property("region", th.StringType),
            th.Property("city", th.StringType),
            th.Property("dma", th.IntegerType),
            th.Property("carrier", th.StringType),
            th.Property("platform", th.StringType),
            th.Property("os_version", th.StringType),
            th.Property("device_type", th.StringType),
            th.Property("device_model", th.StringType),
            th.Property("brand", th.StringType),
            th.Property("browser", th.StringType),
            th.Property("language", th.StringType),
            th.Property("http_user_agent", th.StringType),
            th.Property("adv1", th.StringType),
            th.Property("adv2", th.StringType),
            th.Property("adv3", th.StringType),
            th.Property("adv4", th.StringType),
            th.Property("adv5", th.StringType),
            th.Property("is_event", th.BooleanType),
            th.Property("event", th.StringType),  # Base
            th.Property("notes", th.StringType),
            th.Property("transaction_id", th.StringType),
            th.Property("click_unix_timestamp", th.IntegerType),
            th.Property("error_code", th.IntegerType),
            th.Property("error_message", th.StringType),
            th.Property("sale_amount", th.IntegerType),
            th.Property("is_scrub", th.BooleanType),
            th.Property("coupon_code", th.StringType),
            th.Property("order_id", th.StringType),
            th.Property("url", th.StringType),
            th.Property("isp", th.StringType),
            th.Property("referer", th.StringType),
            th.Property("app_id", th.StringType),
            th.Property("idfa", th.StringType),
            th.Property("idfa_md5", th.StringType),
            th.Property("idfa_sha1", th.StringType),
            th.Property("google_ad_id", th.StringType),
            th.Property("google_ad_id_md5", th.StringType),
            th.Property("google_ad_id_sha1", th.StringType),
            th.Property("android_id", th.StringType),
            th.Property("android_id_md5", th.StringType),
            th.Property("android_id_sha1", th.StringType),
            th.Property("currency_id", th.StringType),
            th.Property("email", th.StringType),
            th.Property("is_view_through", th.BooleanType),
            th.Property("previous_network_offer_id", th.IntegerType),
            th.Property(
                "relationship",
                th.ObjectType(
                    schemas.RelationshipOfferProperty,
                    schemas.RelationshipAdvertiserProperty,
                    schemas.RelationshipAccountManagerProperty,
                    schemas.RelationshipAffiliateProperty,
                    schemas.RelationshipAffiliateManagerProperty,
                    schemas.RelationshipQueryParamsProperty,
                    th.Property("attribution_method", th.StringType),  # unknown
                    th.Property("usm_data", th.AnyType),
                ),
            ),
            th.Property("network_offer_payout_revenue_id", th.IntegerType),
        ).to_dict()

    @override
    def prepare_request_payload(self, context, next_page_token):
        start_value: int | str = self.get_starting_replication_key_value(context)
        start_date = (
            datetime.fromtimestamp(start_value, tz=timezone.utc)
            if isinstance(start_value, int)
            else datetime.fromisoformat(start_value).astimezone(timezone.utc)
        )

        return {
            "from": start_date.strftime(r"%Y-%m-%d %H:%M:%S"),
            "to": datetime.now(tz=timezone.utc).strftime(r"%Y-%m-%d %H:%M:%S"),
            "timezone_id": self.utc_timezone_id,
            "show_conversions": True,
            "show_events": True,
        }


class ClicksStream(EverflowStream):
    """Define clicks stream."""

    name = "clicks"
    primary_keys = ("transaction_id",)
    replication_key = "unix_timestamp"
    http_method = "POST"
    path = "/networks/reporting/clicks/stream"
    records_jsonpath = "$.clicks[*]"

    @override
    def get_new_paginator(self):
        return ClicksPaginator(self)

    @override
    @cached_property
    def schema(self):
        return th.PropertiesList(
            th.Property("transaction_id", th.StringType),
            th.Property("is_unique", th.IntegerType),
            th.Property("unix_timestamp", th.IntegerType),
            th.Property("tracking_url", th.StringType),
            th.Property("source_id", th.StringType),
            th.Property("sub1", th.StringType),
            th.Property("sub2", th.StringType),
            th.Property("sub3", th.StringType),
            th.Property("sub4", th.StringType),
            th.Property("sub5", th.StringType),
            th.Property("payout_type", th.StringType),  # CPA, CPC
            th.Property("revenue_type", th.StringType),  # RPA, RPC
            th.Property("payout", th.NumberType),
            th.Property("revenue", th.NumberType),
            th.Property("referer", th.StringType),
            th.Property("previous_network_offer_id", th.IntegerType),
            th.Property("error_code", th.IntegerType),
            th.Property("project_id", th.StringType),
            th.Property("user_ip", th.StringType),
            th.Property("error_message", th.StringType),
            th.Property("url", th.StringType),
            th.Property("is_view_through", th.BooleanType),
            th.Property("is_async", th.BooleanType),
            th.Property("server_side_url", th.StringType),
            th.Property("server_side_output", th.StringType),
            th.Property("custom_landing_page_id", th.IntegerType),
            th.Property("is_test_mode", th.BooleanType),
            th.Property("idfa", th.StringType),
            th.Property("idfa_md5", th.StringType),
            th.Property("idfa_sha1", th.StringType),
            th.Property("google_ad_id", th.StringType),
            th.Property("google_ad_id_md5", th.StringType),
            th.Property("google_ad_id_sha1", th.StringType),
            th.Property("android_id", th.StringType),
            th.Property("android_id_md5", th.StringType),
            th.Property("android_id_sha1", th.StringType),
            th.Property("error_filter_id", th.StringType),
            th.Property("has_conversion", th.BooleanType),
            th.Property("is_pass_through", th.BooleanType),
            th.Property("creative_id", th.IntegerType),
            th.Property(
                "relationship",
                th.ObjectType(
                    schemas.RelationshipOfferProperty,
                    schemas.RelationshipAdvertiserProperty,
                    schemas.RelationshipAccountManagerProperty,
                    schemas.RelationshipAffiliateProperty,
                    schemas.RelationshipAffiliateManagerProperty,
                    th.Property(
                        "geolocation",
                        th.ObjectType(
                            th.Property("country_code", th.StringType),
                            th.Property("country_name", th.StringType),
                            th.Property("region_code", th.StringType),
                            th.Property("region_name", th.StringType),
                            th.Property("city_name", th.StringType),
                            th.Property("dma", th.IntegerType),
                            th.Property("dma_name", th.StringType),
                            th.Property("timezone", th.StringType),
                            th.Property("carrier_name", th.StringType),
                            th.Property("carrier_code", th.IntegerType),
                            th.Property("organization", th.StringType),
                            th.Property("isp_name", th.StringType),
                            th.Property("is_mobile", th.BooleanType),
                            th.Property("is_proxy", th.BooleanType),
                            th.Property("postal_code", th.StringType),
                        ),
                    ),
                    th.Property(
                        "device_information",
                        th.ObjectType(
                            th.Property("is_mobile", th.BooleanType),
                            th.Property("platform_name", th.StringType),
                            th.Property("os_version", th.StringType),
                            th.Property("brand", th.StringType),
                            th.Property("model", th.StringType),
                            th.Property("is_tablet", th.BooleanType),
                            th.Property("browser_name", th.StringType),
                            th.Property("browser_version", th.StringType),
                            th.Property("device_type", th.StringType),
                            th.Property("language", th.StringType),
                            th.Property("http_accept_language", th.StringType),
                            th.Property("is_robot", th.BooleanType),
                            th.Property("is_filter", th.BooleanType),
                        ),
                    ),
                    th.Property("http_user_agent", th.StringType),
                    th.Property("http_accept_language", th.StringType),
                    schemas.RelationshipQueryParamsProperty,
                    th.Property("previous_transaction_id", th.StringType),
                    th.Property("redirect_url", th.StringType),
                    th.Property("forensiq_score", th.StringType),
                    th.Property(
                        "internal_redirect",
                        th.ObjectType(
                            th.Property("previous_transaction_id", th.StringType),
                            th.Property("previous_offer_id", th.IntegerType),
                            th.Property("is_pay_affiliate", th.BooleanType),
                            th.Property("is_pass_through", th.BooleanType),
                            th.Property("network_offer_url_id", th.IntegerType),
                            th.Property("redirect_count", th.IntegerType),
                        ),
                    ),
                ),
            ),
            th.Property("coupon_code", th.StringType),
            th.Property("redirect_method", th.StringType),  # standard
            th.Property("is_sdk_click", th.BooleanType),
            th.Property("category_id", th.IntegerType),
            th.Property("currency_id", th.StringType),
        ).to_dict()

    @override
    def prepare_request_payload(self, context, next_page_token):
        start_value: datetime | int | str = (
            next_page_token or self.get_starting_replication_key_value(context)
        )

        if isinstance(start_value, datetime):  # from paginator
            start_date = start_value
        elif isinstance(start_value, int):  # from state
            start_date = datetime.fromtimestamp(start_value, tz=timezone.utc)
        else:  # from config
            start_date = datetime.fromisoformat(start_value).astimezone(timezone.utc)

        now = datetime.now(tz=timezone.utc)

        # min from date is ~3 months from the current date, i.e. approx. 90 days
        # https://developers.everflow.io/docs/network/reporting/raw_clicks/#click-report
        from_date = max(start_date, now - timedelta(days=90))

        # max to date is 14 days from start date, i.e. period of 2 weeks
        # https://developers.everflow.io/docs/network/reporting/raw_clicks/#click-report
        to_date = min(from_date + timedelta(days=14), now)

        self.logger.info("Requesting clicks from %s to %s", from_date, to_date)

        return {
            "from": from_date.strftime(r"%Y-%m-%d %H:%M:%S"),
            "to": to_date.strftime(r"%Y-%m-%d %H:%M:%S"),
            "timezone_id": self.utc_timezone_id,
        }
