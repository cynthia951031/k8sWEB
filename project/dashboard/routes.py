# encoding: utf-8
from flask import render_template, flash, redirect, url_for, abort,\
    request, current_app, g, jsonify

from flask_login import login_required, current_user
from .. import db
from ..models import User
from .forms import CreateForm, UpdateForm, DeleteForm, QueryForm

@dashboard.route('/<userid>', methods=['GET'])
@login_required
def home(userid):
    user = User.query.filterby(userid).first_or_404()
    page = request.args.get('page', 1, type=int)
    pagination = user.instances.order_by(Instance.postStamp.desc()).item
    instance_list = pagination.items
    if user == current_user:
    	return render_template('dashboard/home.html', userid=userid, instances=instances_list,
    							pagination=pagination)
	return render_template('dashboard/home.html', userid=userid)


@dashboard.route('/create', methods=['POST', 'GET'])
@login_required
def create():
	form = CreateForm()
	if form.validate_on_submit():
		instance = Instance(author=current_user)
		form.to_model(instance)
		db.session.add(instance)
		db.session.commit()
		#TODO: connection with the service and give the service ip & port
		#also needs to reply the flash()
		return redirect(url_for('.create'))
	return render_template('dashboard/create.html', form=form)

@dashboard.route('/update', methods=['POST', 'GET'])
@login_required
def update():
	form = UpdateForm()
	if form.validate_on_submit():
		tobeUpdate = form.instance_id.data
		newScale = form.insScale.data
		#TODO: connection with the service and give the service ip & port
		#also needs to reply the flash()
		return redirect(url_for('.update'))
	return render_template('dashboard/update.html',form=form)


