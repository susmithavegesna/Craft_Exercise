"""Surface details about the API"""

class ServiceDetails:
    """Details controller"""

    @classmethod
    def get_details(cls):
        """Get details"""
        return {
            "api_version": "0.1",
            "app": "Craft Exercise",
            "env": "dev"
        }
