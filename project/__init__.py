from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

login_manager = LoginManager()
login_manager.login_view = 'user.login'
db = SQLAlchemy()
Bootstrap = Bootstrap()

def create_app(config_name):
	app = Flask(__name__, static_url_path='/static')
	app.config.from_object(config[config_name])

	db.init_app(app)
	Bootstrap.init_app(app)
	login_manager.init_app(app)

	from .util import interface_blueprint
	app.register_blueprint(interface_blueprint)

	from .user import user as user_blueprint
	app.register_blueprint(user_blueprint, url_prefix='/user')

	from .dashboard import dashboard as dashboard_blueprint
	app.register_blueprint(dashboard_blueprint, url_prefix='/dashboard')

	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)
	
	with app.app_context():
		db.create_all()

	return app