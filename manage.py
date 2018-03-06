# coding:utf-8
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db
import multiprocessing, time
# 引入数据库数据表模型
from flask_migrate import upgrade


app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

# Global variables to jiajia2 environment:==设置为全局变量 在HTML里可以直接使用以下参数
# app.jinja_env.globals['School'] = School


# def make_shell_context():
#     return dict(db=db, User=User,
#                 Orders=Orders, Course=Course,
#                 Address=Address, TagList=TagList,
#                 Tag=Tag, Tags=Tags,
#                 Collect=Collect, Comment=Comment, BuyCar=BuyCar,
#                 Detail=Detail, UserLog=UserLog
#                 )
#
#
# manager.add_command("shell", Shell(make_context=make_shell_context))
#
#
# @manager.command
# def deploy():
#     # 创建所需数据表
#     db.create_all()
#     upgrade()


if __name__ == '__main__':
    # 开启多线程
    manager.run()