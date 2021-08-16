"""Base Schemas"""
from marshmallow import fields
from marshmallow.schema import Schema


class BaseApiError(Schema):
    """API Error serializer."""

    msg = fields.Str(required=True, strict=True)
    errors = fields.List(fields.Str, required=False, strict=True)


class BaseSchema(Schema):
    """Base schema class

    Subclass this for all schemas that require an auto-generated
    Meta.title attribute.
    """

    def __init__(self, *args, **kwargs):
        """Override any application wide schema defaults here"""
        super().__init__(*args, **kwargs)


class ApiErrorSchema(BaseSchema, BaseApiError):
    """APIError marshmallow serializer"""


class BadRequest(Exception):
    """Custom exception class to be thrown when local error occurs."""
    def __init__(self, message, status=400, payload=None):
        self.message = message
        self.status = status
        self.payload = payload


