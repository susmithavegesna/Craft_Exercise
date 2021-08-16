"""Application blueprints"""
from api_template.blueprints import healthcheck
from api_template.blueprints import service


class AppBlueprints:
    """Application blueprints"""

    def __init__(self, app):
        """Registerer blueprints"""
        app.register_blueprint(
            healthcheck.healthcheck,
            url_prefix="/healthcheck",
        )

        app.register_blueprint(
            service.service,
            url_prefix="/details",
        )
