"""Flask application"""

from flask import Flask
from flask_compress import Compress
from werkzeug.debug import DebuggedApplication
from api_template.extentions.error_handlers import AppErrors
from api_template.extentions.app_blueprints import AppBlueprints


def application():
    """Flask application"""

    #########################################
    # Initialize Flask App
    #########################################

    app = Flask(__name__)

    app.extensions = {}

    Compress(app)


    #########################################
    # Custom Error Handlers
    #########################################

    AppErrors(app)

    #########################################
    # Endpoint Definitions and Blueprints
    #########################################

    AppBlueprints(app)

    ##########################################################################
    # Attached debug wsgi app for when behind gunicorn
    ##########################################################################

    if app.debug:
        print("Attaching Debugger")
        app.wsgi_app = DebuggedApplication(
            app.wsgi_app,
            pin_security=False,
            evalex=True,
        )

    print("API Configured")
    return app

if __name__ == "__main__":
    application().run(host="0.0.0.0", port=5000)