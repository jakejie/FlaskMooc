# coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_wtf.csrf import CsrfProtect,CSRFProtect
# from fla import CsrfProtect
from flask_moment import Moment
from config import Config
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class

db = SQLAlchemy()
bootstrap = Bootstrap()
# moment = Moment()
# 登陆管理
login_manager = LoginManager()
login_manager.session_protection = 'strong'
# 指定默认的登陆页面
login_manager.login_view = 'auth.login'

csrf = CSRFProtect()
# photos = UploadSet('photos', IMAGES)


# static_folder = '',, static_url_path=''
def create_app():
    app = Flask(__name__, static_url_path='')
    app.config.from_object(Config)
    Config.init_app(app)
    csrf.init_app(app)

    db.init_app(app)
    bootstrap.init_app(app)
    # moment.init_app(app)
    login_manager.init_app(app)

    # 登陆提示信息
    login_manager.login_message = u'对不起，您还没有登录'
    login_manager.login_message_category = 'info'

    # configure_uploads(app, photos)
    # patch_request_class(app)

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix="/admin")

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .course import course as home_blueprint
    app.register_blueprint(home_blueprint, url_prefix='/course')

    from .organization import organization as home_blueprint
    app.register_blueprint(home_blueprint, url_prefix='/organization')

    from .teachers import teachers as home_blueprint
    app.register_blueprint(home_blueprint, url_prefix='/teachers')

    from .users import users as home_blueprint
    app.register_blueprint(home_blueprint, url_prefix='/users')

    from .index import index as home_blueprint
    app.register_blueprint(home_blueprint)
    return app
