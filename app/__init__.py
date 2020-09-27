from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'aith.login'


def create_app():
	app = Flask(__name__)
	app.config.from_object(Config)
	from .auth import auth as authentication_blueprint

    app.register_blueprint(authentication_blueprint)



	bootstrap.init_app(app)
	db.init_app(app)
	login_manager.init_app(app)



	return app