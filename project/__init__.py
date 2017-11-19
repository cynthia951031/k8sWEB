from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.
db = SQLAlchemy()


def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	'''if not app.config['DEBUG'] and not app.config_name['TESTING']:
		import logging
		from logging.handlers import SysLogHandler
		syslog_handler = SysLogHandler()
		syslog_handler.setLevel(logging.WARNING)
		app.logger.addHandler(syslog_handler)
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True'''

	db.init_app(app)
	login_manager.init_app(app)

	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint, url_prefix='/auth')

	from .dashboard import dashboard as dashboard_blueprint
	app.register_blueprint(dashboard_blueprint, url_prefix='/dashboard')

	with app.app_context():
		db.create_all()

	return app