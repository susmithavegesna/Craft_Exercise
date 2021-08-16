"""HealthCheck Blueprint"""
from flask import Blueprint
from flask_apispec import marshal_with
from api_template.controllers.service_details import ServiceDetails
from api_template.serializers.service import ServiceDetails as ServiceDetailsSchema

service = Blueprint("service", __name__)


# Endpoints
@service.route("", methods=["GET"])
@marshal_with(ServiceDetailsSchema, code=200)
def service_details():
    """Service details endpoint"""
    return ServiceDetails.get_details(), 200
