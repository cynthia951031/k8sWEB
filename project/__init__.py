from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'user.login'
db = SQLAlchemy()


def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])

	#config init 
	#config[config_name].init_app(app)

	'''if not app.config['DEBUG'] and not app.config_name['TESTING']:
		import logging
		from logging.handlers import SysLogHandler
		syslog_handler = SysLogHandler()
		syslog_handler.setLevel(logging.WARNING)
		app.logger.addHandler(syslog_handler)
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True'''

	db.init_app(app)
	login_manager.init_app(app)

	from .util import interface_blueprint
	app.register_blueprint(interface_blueprint)

	from .user import user as user_blueprint
	app.register_blueprint(user_blueprint, url_prefix='/user')

	from .dashboard import dashboard as dashboard_blueprint
	app.register_blueprint(dashboard_blueprint, url_prefix='/dashboard')

	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	'''with app.app_context():
		db.create_all()'''

	return app