from . import index
from flask import render_template, flash, redirect, request, session, url_for
from flask_login import login_required, current_user


@index.route('/')
def index():
    return "主页哦"
