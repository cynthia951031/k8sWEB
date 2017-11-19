# encoding: utf-8
from flask import render_template, current_app, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app import db
from ..models import User
from . import user
from .forms import LoginForm, RegisterForm


@user.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("user/login.html", title = u'用户登录')
    elif request.method == 'POST':
        '''if not current_app.config['DEBUG'] and not current_app.config['TESTING'] \
                and not request.is_secure:
            return redirect(url_for('.login', _external=True, _scheme='https'))'''
    #创建表单
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(id=form.user_id.data).first()
            # 验证表单，如果正确重定向到dashboard
            if user is None or not user.verify_password(form.password.data):
               flash(u'用户ID或密码错误')
               return redirect(url_for('.login'))
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('dashboard.home', userid=user.id))

@user.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('user/register.html', title = u'账号注册')
    elif request.method == 'POST':
        '''if not current_app.config['DEBUG'] and not current_app.config['TESTING'] \
                and not request.is_secure:
            return redirect(url_for('.login', _external=True, _scheme='https'))'''
        # 创建表单
        form = RegisterForm()
        # 提交注册
        if form.validate_on_submit() and form.password.data==form.password_confirm.data:
            if form.password.data != form.password_confirm.data:
                flash(u'两次输入密码不一致')
                return redirect(url_for('.register'))
            else:
                user = User(name=form.user_name.data, password=form.password.data)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect(request.args.get('next') or url_for('dashboard.home', userid = user.id))



@user.route('/logout')
@login_required
def logout():
    logout_user()
    flash(u'您已退出登录')
    return redirect(url_for('.login'))

