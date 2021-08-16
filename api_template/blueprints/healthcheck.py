"""HealthCheck Blueprint"""
from flask import Blueprint
from flask_apispec import marshal_with
from api_template.serializers.healthcheck import HealthCheck

healthcheck = Blueprint("healthcheck", __name__)


# Endpoints
@healthcheck.route("", methods=["GET"])
@marshal_with(HealthCheck, code=200)
def get_healthcheck():
    """Healthcheck endpoint"""
    return {"status": "healthy"}, 200
