from . import auth
from flask import render_template, flash, redirect, request, session, url_for
from flask_login import login_required, current_user
from .forms import RegisterForm, LoginForm, FindPasswordForm, ResetPasswordForm, gene_code
import time


# 注册
@auth.route('/register/', methods=["POST", 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print(request.form)
        print(request.form["username"])
        print(request.form["email"])
        print(request.form["password"])
        return "注册成功"
    else:
        return render_template('auth/register.html', form=form)


# 登陆
@auth.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(request.form)
        print(request.form["username"])
        print(request.form["email"])
        print(request.form["password"])
        return "登陆成功"
    else:
        return render_template('auth/login.html', form=form)
        # return "登陆"


# 找回密码
@auth.route('/forgetpwd', methods=["POST", "GET"])
def forgetpwd():
    form = FindPasswordForm()
    if form.validate_on_submit():
        print(request.form)
        print(request.form["username"])
        print(request.form["email"])
        return redirect(url_for('auth.password_reset'))
    else:
        return render_template('auth/forgetpwd.html', form=form)


# 重置密码
@auth.route('/password_reset', methods=["POST", "GET"])
def password_reset():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        print(request.form)
        print(request.form["password"])
        print(request.form["re_password"])
        return "重置密码拉"
    else:
        return render_template('auth/password_reset.html', form=form)


# 修改密码
@auth.route('/changepwd', methods=["POST", "GET"])
def changepwd():
    pass


# 生成验证码图片
@auth.route('/get_code')
def get_code():
    file_name = time.time()
    image = gene_code(file_name)
    # 将图片验证码写入数据表进行进一步验证
    return "{}".format(image)
