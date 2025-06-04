"""JSON schema files for the REST API."""

from singer_sdk import typing as th

RelationshipOfferProperty = th.Property(
    "offer",
    th.ObjectType(
        th.Property("network_offer_id", th.IntegerType),
        th.Property("network_id", th.IntegerType),
        th.Property("network_advertiser_id", th.IntegerType),
        th.Property("network_offer_group_id", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property(
            "offer_status",
            th.StringType,
        ),  # active, deleted
        th.Property("network_tracking_domain_id", th.IntegerType),
        th.Property("visibility", th.StringType),  # private
        th.Property("currency_id", th.StringType),
    ),
)

RelationshipAdvertiserProperty = th.Property(
    "advertiser",
    th.ObjectType(
        th.Property("network_advertiser_id", th.IntegerType),
        th.Property("network_id", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property(
            "account_status",
            th.StringType,
        ),  # active, inactive
    ),
)

RelationshipAccountManagerProperty = th.Property(
    "account_manager",
    th.ObjectType(
        th.Property("network_employee_id", th.IntegerType),
        th.Property("network_id", th.IntegerType),
        th.Property("first_name", th.StringType),
        th.Property("last_name", th.StringType),
        th.Property("full_name", th.StringType),
        th.Property(
            "account_status",
            th.StringType,
        ),  # active, inactive
    ),
)

RelationshipAffiliateProperty = th.Property(
    "affiliate",
    th.ObjectType(
        th.Property("network_affiliate_id", th.IntegerType),
        th.Property("network_id", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property(
            "account_status",
            th.StringType,
        ),  # active, inactive
        th.Property("network_traffic_source_id", th.IntegerType),
    ),
)

RelationshipAffiliateManagerProperty = th.Property(
    "affiliate_manager",
    RelationshipAccountManagerProperty.wrapped,
)

RelationshipQueryParamsProperty = th.Property(
    "query_parameters",
    th.ObjectType(additional_properties=True),
)
