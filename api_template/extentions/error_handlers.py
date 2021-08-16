"""Register all custom error handlers"""


class AppErrors:
    """Error handlers"""

    def __init__(self, app):
        """Register error handlers"""

        @app.errorhandler(404)
        def page_not_found(e):
            """Page not found as json"""
            error = str(e)
            return {
                "msg": error,
                "app": 'Craft Exercise',
                "api_version": 0.1,
            }
