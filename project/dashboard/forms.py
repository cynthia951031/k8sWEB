# encoding: utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Length
from datetime import datetime


class CreateForm(FlaskForm):
	instance_name = StringField(u'实例名称', validators=[DataRequired(), Length(1, 128)])
	CPUsize = DecimalField(u'cpu大小', validators=[DataRequired()])
	MEMsize = DecimalField(u'内存大小', validators=[DataRequired()])
	insScale = IntegerField(u'实例规模', validators=[DataRequired()])
	GPUnum = IntegerField(u'gpu数量', validators=[DataRequired()])
	isSSD = BooleanField(u'是否使用SSD', validators=[DataRequired()])
	submit = SubmitField(u'提交')


class UpdateForm(FlaskForm):
	new_scale = DecimalField(u'实例规模', validators=[DataRequired()])
	submit = SubmitField(u'提交')

class QueryForm(FlaskForm):
	instance_id = IntegerField(u'实例ID', validators=[DataRequired()])
	submit = SubmitField(u'提交')

class DeleteForm(FlaskForm):
	instance_id = IntegerField(u'实例ID', validators=[DataRequired()])
	submit = SubmitField(u'提交')