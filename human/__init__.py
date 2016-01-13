from flask import Flask
from human.views.admin import admin
from human.views.main import main
from human.helpers import static
from human.extensions import db
import human_settings

def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(human_settings)

    if config:
        app.config.from_object(config)

    db.init_app(app)

    @app.context_processor
    def inject_static():
        """Make the static helper function available inside the templates"""
        return dict(static=static)

    app.register_module(admin)
    app.register_module(main)
    return app