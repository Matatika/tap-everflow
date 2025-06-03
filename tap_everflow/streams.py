"""Stream type classes for tap-everflow."""

from __future__ import annotations

from functools import cached_property

from singer_sdk import typing as th
from typing_extensions import override

from tap_everflow.client import EverflowStream


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
            th.Property("relationship", th.ObjectType(additional_properties=True)),
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
