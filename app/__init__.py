from flask import Flask

def create_app():
    app = Flask(__name__,
                static_url_path='',
                static_folder='statics')

    app.config.from_pyfile('settings.cfg')

    from .public import public_bp
    app.register_blueprint(public_bp)

    from .admin import admin_bp
    app.register_blueprint(admin_bp)

    return app