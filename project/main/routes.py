#! /usr/bin/env python
# -*- coding: utf-8 -*-
from . import main
from flask import render_template, jsonify,redirect,url_for
from flask_login import login_required, current_user
from ..util.API_manage import API_URL

@main.route('/')
@login_required
def index():
    return redirect(url_for('user.login'))

@main.app_errorhandler(404)
def page_404(err):
    return render_template('main/404.html', title='404'), 404


@main.app_errorhandler(403)
def page_403(err):
    return render_template('main/403.html', title='403'), 403


@main.app_errorhandler(500)
def page_500(err):
    return render_template('main/500.html', title='500'), 500
