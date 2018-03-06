# coding:utf-8
from app import db, login_manager
import hashlib
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
import time

# 用户表
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)  # 序号
    email = db.Column(db.String(64), unique=True, index=True)  # 邮箱
    phone = db.Column(db.String(11), unique=True)  # 手机号码
    username = db.Column(db.String(128), unique=True, index=True)  # 用户名
    birthday = db.Column(db.DATE)  # 出生日期
    sex = db.Column(db.String(32))  # 性别
    password = db.Column(db.String(256))  # 密码
    pwd = db.Column(db.String(256))
    password_hash = db.Column(db.String(128), unique=True)  # 密码 哈希
    avatar_hash = db.Column(db.String(32))
    image = db.Column(db.TEXT)  # 图像
    account_atatus = db.Column(db.String(4))  # 账号状态
    activate = db.Column(db.String(4), default="1")  # 1表示未激活 2表示已经激活
    ac_type = db.Column(db.String(4), default="1")  # 1表示普通用户 2表示管理员后台账号
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 注册时间
    info = db.Column(db.Text)  # 个性简介
    member_grade = db.Column(db.String(4), default="0")  # 会员等级
    account_point = db.Column(db.Integer, default=0)  # 会员积分
    uuid = db.Column(db.String(1024))
    # （设置外键的第二步）
    # users_id = db.relationship('Address')  # 会员收货地址外键关系关联
    # user_order = db.relationship('Orders')  # 订单信息外键关系关联
    # comment_user = db.relationship('Comment', backref='user')  # 会员评论信息外键关系关联
    # user_logs = db.relationship('UserLog', backref='user')  # 会员登陆日志信息外键关系关联
    # user_message = db.relationship('Message', backref='user')  # 会员登陆日志信息外键关系关联
    # user_car = db.relationship('BuyCar')  # 购物车外键关系关联
    # detail_user = db.relationship('Detail')  # 订单商品购买人 外键关系关联
    # col_user = db.relationship('Collect', backref='user')  # 收藏商品对应用户

    def __repr__(self):
        return '<User %r>' % self.username

    @staticmethod
    def insert_admin(email, phone, username, password, ac_type="2", activate="2"):
        user = User(email=email, phone=phone, username=username,
                    password=password, ac_type=ac_type, activate=activate)
        db.session.add(user)
        db.session.commit()

    # @property
    # def password(self):
    #     raise AttributeError('password is not a readable attribute')
    #
    # @password.setter
    # def password(self, password):
    #     self.password_hash = generate_password_hash(password)
    #
    # def verify_password(self, password):
    #     return check_password_hash(self.password_hash, password)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.email is not None and self.avatar_hash is None:
            self.avatar_hash = hashlib.md5(
                self.email.encode('utf-8')).hexdigest()

    def gravatar(self, size=40, default='identicon', rating='g'):
        pass

    def check_pwd(self, password):  # 检验密码
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, password)

    def check_user(self, username):  # 检验用户名是否存在
        count = User.query.filter_by(username=username).count()
        if count == 1:
            return True
        else:
            return False