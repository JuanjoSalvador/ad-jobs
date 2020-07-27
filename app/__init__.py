from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app import config

app = Flask(__name__,
        static_url_path='',
        static_folder='statics')

app.config.from_object(config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

db.init_app(app)

def create_app():

    from .public import public_bp
    app.register_blueprint(public_bp)

    from .admin import admin_bp
    app.register_blueprint(admin_bp)
     
    return app

def register_error_handlers(app):

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.jinja'), 404