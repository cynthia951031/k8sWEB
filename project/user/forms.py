# encoding: utf-8
from flask_wtf import FlaskForm
from wtforms import IntegerField,StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    user_id = IntegerField(u'用户ID', validators=[DataRequired()])
    password = PasswordField(u'密码', validators=[DataRequired()])
    remember_me = BooleanField(u'记住我')
    submit = SubmitField(u'登录')


class RegisterForm(FlaskForm):
    user_name = IntegerField(u'用户名', validators=[DataRequired()])
    password = PasswordField(u'密码', validators=[DataRequired()])
    password_confirm = PasswordField(u'密码确认', validators=[DataRequired()])
    submit = SubmitField(u'注册')
