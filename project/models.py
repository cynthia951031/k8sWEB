from . import db, login_manager
from datetime import datetime
import hashlib
from flask import request, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
'''
user_instance = db.Table('user_instance', 
				db.Column(('user_id'), db.Integer, db.ForeignKey(user.id)),
				db.Column(('instance_id'), db.Integer, db.ForeignKey(instance.id))
				)

app_instance = db.Table('app_instance',
				db.Column(('app_id'), db.Integer, db.ForeignKey(app.id)),
				db.Column(('instance_id'), db.Integer, db.ForeignKey(instance.id))
				)'''

class User(db.model):
	__tabelname__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), nullable = False)
	password = db.Column(db.String(64), nullable = False)
	#instances = db.relationship('Instance', backref='author', lazy='dynamic')

	def __init__(self, **kwargs):
		super(User, self).__init__(**kwargs)
		if self.avatar_hash is None and self.name is not None:
			self.avatar_hash = hashlib.md5(self.name.encode('utf-8')).hexdigest()
	
	"""以下三个函数分别用于对用户密码进行读取保护、散列化以及验证密码"""
	@property
	def password(self):
		raise AttributeError('password is not a readble attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	"""以下两个函数用于token的生成和校验"""
	def get_api_token(self, expiration=300):
		s = Serializer(current_app.config['SECRET_KEY'], expiration)
		return s.dumps({'user':self.id}).decode('utf-8')

	@staticmethod
	def validate_api_token(token):
		s = Serializer(current_app.config['SECRET_KEY'])
		try:
			data = s.loads(token)
		except:
			return None
		id = data.get('user')
		if id:
			return User.query.get(id)
		return None


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))
'''
class Instance(db.model):
	__tabelname__ = 'instance'
	id = db.Column(db.Integer, primary_key=True, nullable=False)
	name = db.Column(db.String(128), nullable=False)
	CPUsize = db.Column(db.Integer, nullable=False)
	MEMsize = db.Column(db.Float, nullable=False)
	GPUnum = db.Column(db.Integer, nullable=False)
	insScale = db.Column(db.Integer, nullable=False) # the scale of pods
	isSSD = db.Column(db.Boolean, default=True, nullable=False)
	postStamp = db.Column(db.DataTime)
	serviceIP = db.Column(db.Text)
	servicePort = db.Column(db.Integer)
	updateStamp = db.Column(db.DataTime)
	deleteStamp = db.Column(db.DataTime)

	user_id = db.Column(db.Integer, db.ForeignKey(user.id))
	app_id = db.Column(db.Integer, db.ForeignKey(app.id), nullable=False)


class App(db.model):
	__tabelname__ = 'app'
	id = db.Column(db.Integer, primary_key=True, nullable=False)
	name = db.Column(db.Integer, nullable=False)'''
	







	