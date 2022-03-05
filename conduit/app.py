import os

from flask import Flask

# incase there is more than one name
# get the first name split by a dot
app_name = __name__.split(".")[0]


def create_app():
    app = Flask(app_name, instance_relative_config=True)
    # create_folders for enviroment
    create_folders(app)

    # register extensions
    attach_extensions(app)

    # register the blueprints
    attach_blueprints(app)

    # we return the app to get through run_app
    return app


def attach_extensions(app):
    from conduit.extensions import cors

    cors.init_app(app, origins="/*")


def attach_blueprints(app):
    from conduit.views.user import bp as user_bp

    app.register_blueprint(user_bp)


def create_folders(app):
    # checks environment first
    # default will be DEVELOPMENT if no enviroment exists on os.environ
    env = os.environ.get("ENVIRONMENT", "DEVELOPMENT")

    if env == "DEVELOPMENT":
        try:
            os.mkdir(app.instance_path)
        except OSError:
            pass
