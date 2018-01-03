# encoding: utf-8
from flask import render_template, flash, redirect, url_for, abort, request, current_app, g, jsonify
from datetime import datetime
from flask_login import login_required, current_user
from .. import db
from ..models import User
from .forms import CreateForm, UpdateForm, DeleteForm, QueryForm
from ..util.API_manage import ApiClient
from . import dashboard
import json


@dashboard.route('home/<int:userid>', methods=['GET', 'POST'])
@login_required
def home(userid):
	login_data = dict(name = current_user.name, id = current_user.id)
	#  TODO: replace debug code with api_client
 	#
 	#  ==========================================================================
 	# api_client = ApiClient(login_data=login_data)
 	# api_client.login()
 	# data = api_client.get_instances_list()
 	# ins_list = [dict(name = ins.name, id = ins.id, is_deleted = ins.is_deleted, update_time = ins.update_time)\
 	# 			 for ins in json.loads(data)['ins_list']]
 	#  ==========================================================================
 
 	# WARNING: This is an example for the value of api_client function,need to be replaced;
 	# ===========================================================================
 	ins_list = [dict(name = "test.name1", id = 1, is_deleted = False, update_time = 100)]
 	# ===========================================================================
	return render_template('dashboard/home.html',
							userid=userid,
							ins_list = ins_list)

@dashboard.route('/detail/<int:iid>', methods=['GET', 'POST'])
@login_required
def detail(iid):
	login_data = dict(name = current_user.name, id = current_user.id)
	api_client = ApiClient(login_data=login_data)
	api_client.login()
	data = api_client.get_instance_detail(iid=iid)
	#具体返回参数看 k8sAPI！！！
	#交给前端解析，注意区分 id 和 uid，实际上用户查询更新删除依赖的是 id 而非 uid
	param = json.loads(data) # 应该是dict
	return render_template("dashboard/instance/detail.html",
							param = param)

@dashboard.route('/create', methods=['POST','GET'])
@login_required
def create():
	form = CreateForm()
	if form.validate_on_submit():
		login_data = dict(name = current_user.name, id = current_user.id)
		# TODO: replace debug code with api_client
 		# =============================================================================
 		# api_client = ApiClient(login_data=login_data)
 		# api_client.login()
 		# r_status = api_client.create_instance(name = form.instance_name.data,
 		# 									cpu = form.CPUsize.data,
 		# 									mem = form.MEMsize.data,
 		# 									scale = form.insScale.data,
 		# 									gpu = form.GPUnum.data,
 		# 									isSSD = form.isSSD.data)
 		# if r_status == 200:
 		# 	flash('created')
 		# 	return redirect(url_for('.home'))
 		# =============================================================================
	return render_template('dashboard/create.html', form=form)

@dashboard.route('/update/<int:iid>', methods=['POST', 'GET'])
@login_required
def update(iid):
	form = UpdateForm()
	if form.validate_on_submit():
		login_data = dict(name = current_user.name, id = current_user.id)
		api_client = ApiClient(login_data=login_data)
		api_client.login()
		r_status = api_client.update_instance(iid=iid, new_scale = form.new_scale.data)
		if r_status == 200:
			flash('updated')
			return redirect(url_for('.home'))
	return render_template('dashboard/update.html', form=form)

@dashboard.route('/delete/<int:iid>', methods=['POST', 'GET'])
@login_required
def delete(iid):
	form = DeleteForm()
	if form.validate_on_submit():
		login_data = dict(name = current_user.name, id = current_user.id)
		api_client = ApiClient(login_data=login_data)
		api_client.login()
		r_status = api_client.delete_instance(iid=iid)
		if r_status == 200:
			flash('deleted')
			return redirect(url_for('.home'))
	return render_template('dashboard/delete.html', form=form)






