# encoding: utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Length
from datetime import datetime


class CreateForm(FlaskForm):
	instance_id = IntegerField(u'实例ID', validators=[DataRequired()])
	instance_name = StringField(u'实例名称', validators=[DataRequired(), Length(1, 128)])
	CPUsize = DecimalField(u'cpu大小', validators=[DataRequired()])
	MEMsize = DecimalField(u'内存大小', validators=[DataRequired()])
	insScale = IntegerField(u'实例规模', validators=[DataRequired()])
	GPUnum = IntegerField(u'gpu数量', validators=[DataRequired()])
	isSSD = BooleanField(u'是否使用SSD', validators=[DataRequired()])
    app_id = DecimalField(u'应用ID', validators=[DataRequired()])

    submit = SubmitField(u'提交')

    def to_model(self, instance):
    	instance.id = self.instance_id
    	instance.name = self.instance_name
    	instance.CPUsize = self.CPUsize
    	instacne.MEMsize = self.MEMsize
    	instance.insScale = self.insScale
    	instance.GPUnum = self.GPUnum
    	instance.isSSD = self.isSSD
    	instance.postStamp = datetime.now() #depends on k8s whether return the timestamp

    def from_model(self, instance):
    	self.instance_id.data = instance.id
    	self.instance_name.data = instance.name
    	self.CPUsize.data = instance.CPUsize
    	self.MEMsize.data = instance.MEMsize
    	self.insScale.data = instance.insScale
    	self.GPUnum.data = instance.GPUnum
    	self.isSSD.data = instance.isSSD
    	self.app_id.data = instance.app_id

class UpdateForm(FlaskForm):
	instance_id = IntegerField(u'实例ID', validators=[DataRequired()])
	new_scale = DecimalField(u'实例规模', validators=[DataRequired()])
	submit = SubmitField(u'提交')

class QueryForm(FlaskForm):
	instance_id = IntegerField(u'实例ID', validators=[DataRequired()])
	submit = SubmitField(u'提交')

class DeleteForm(FlaskForm):
	instance_id = IntegerField(u'实例ID', validators=[DataRequired()])
	submit = SubmitField(u'提交')