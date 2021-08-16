"""Serializer Objects"""
from marshmallow import fields
from api_template.serializers.base import BaseSchema


class ServiceDetails(BaseSchema):
    """HealthCheck marshmallow serializer"""

    env = fields.Str(
        description="Current environment",
        example="dev",
        required=True,
        strict=True,
    )
    app = fields.Str(
        description="Application name",
        example="Craft Exercise",
        required=True,
        strict=True,
    )
    api_version = fields.Str(
        description="Current deployed version of the api",
        example="0.1",
        required=True,
        strict=True,
    )

