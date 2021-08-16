"""Serializer Objects"""
from marshmallow import fields
from api_template.serializers.base import BaseSchema


class HealthCheck(BaseSchema):
    """HealthCheck marshmallow serializer"""

    status = fields.Str(
        description="State of the API",
        example="healthy",
        required=True,
        strict=True,
    )
