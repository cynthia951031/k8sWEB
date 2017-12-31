# encoding: utf-8
from flask import render_template, flash, redirect, url_for, abort, request, current_app, g, jsonify
from datetime import datetime
from flask_login import login_required, current_user
from .. import db
from ..models import User
from .forms import CreateForm, UpdateForm, DeleteForm, QueryForm
from ..util.utils import get_login_data
from ..util.API_manage import ApiClient
from . import dashboard



@dashboard.route('/<int:userid>', methods=['GET', 'POST'])
@login_required
def home(userid):
	api_client = ApiClient(login_data=get_login_data(current_user))
	api_client.login()
	data = api_client.get_instances_list()
	return render_template('dashboard/home.html', userid=userid,
												instances=data['instances'],
												title='my_instances')


@dashboard.route('/detail/<int:iid>', methods=['GET', 'POST'])
@login_required
def detail(iid):
	api_client = \
		ApiClient(login_data='{"name":"%s", "id":"%s"}' % (current_user.name, current_user.id))
	api_client.login()
	data = api_client.get_instance_detail(iid=iid)
	instance = data['instance']
	config = data['config'][0]
	param = json.loads(data['config'][0]['param'])
	proxy = api_client.get_instance_proxy(iid = iid)
	return render_template("dashboard/instance/detail.html",
							instance = instance, 
							config = config,
							param = param,
							proxy = proxy['Service'],
							title = 'instance_details')

@dashboard.route('/create', methods=['POST'])
@login_required
def create():
	form = CreateForm()
	if form.validate_on_submit():
		api_client = ApiClient(login_data=get_login_data(current_user))
		api_client.login()
		r_status = api_client.create_spark(name = form.instance_name.data, 
											cpu = form.CPUsize.data, 
											mem = form.MEMsize.data,
											scale = form.insScale.data, 
											gpu = form.GPUnum.data, 
											isSSD = form.isSSD.data)
		if r_status == 200:
			flash('created')
			return redirect(url_for('.home'))
	return render_template('dashboard/create.html', title = 'create_instance')

@dashboard.route('/update/<int:iid>', methods=['POST', 'GET'])
@login_required
def update(iid):
	form = UpdateForm()
	if form.validate_on_submit():
		api_client = ApiClient(login_data=get_login_data(current_user))
		api_client.login()
		r_status = api_client.update_instance(iid=iid, new_scale = form.new_scale.data)
		if r_status == 200:
			flash('updated')
			return redirect(url_for('.home'))
	return render_template('dashboard/update.html', title = 'update_instance')



