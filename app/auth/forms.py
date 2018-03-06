from flask_wtf.form import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextField, DateField, PasswordField
from wtforms.validators import DataRequired, ValidationError, Email, Regexp


# DataRequired 检查类型转换后的值，是否为真（即 if field.data）
# InputRequired 检查原始输入的值，是否为真

# 注册
class RegisterForm(FlaskForm):
    # 用户名
    username = StringField(label="用户名")
    # 邮箱
    email = StringField(label="邮&nbsp;箱", description="邮箱")
    # 密码
    password = PasswordField(label="密码")
    # 重新输入密码
    re_password = PasswordField(label="再次输入密码")
    # 生日
    # birthday = DateField(label="生日")
    # 验证码
    # verification_code = StringField(u'验证码', validators=[Required(), Length(4, 4, message=u'填写4位验证码')])
    # 提交
    submit = SubmitField(label="注册")


# 登陆
class LoginForm(FlaskForm):
    # 用户名
    username = StringField(label="用户名")
    # 邮箱
    email = StringField(label="邮箱")
    # 密码
    password = PasswordField(label="密码")



# 找回密码
class FindPasswordForm(FlaskForm):
    # 用户名
    username = StringField(label="用户名")
    # 邮箱
    email = StringField(label="邮箱")



# 重置密码
class ResetPasswordForm(FlaskForm):
    # 密码
    password = PasswordField(label="密码")
    re_password = PasswordField(label="密码")
# 修改密码
class ChangePasswordForm(FlaskForm):
    # 密码
    old_password = PasswordField()
    password = PasswordField(label="密码")
    re_password = PasswordField(label="密码")

# ------------图片验证码生成--------------------------------------------------

# 用来随机生成一个字符串
from random import Random
import sys
import math
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# 字体的位置，不同版本的系统会有不同
font_path = 'C:/Windows/Fonts/Arial.ttf'
# 生成几位数的验证码
number = 4
# 生成验证码图片的宽度和高度
size = (100, 30)
# 背景颜色，默认为白色
bgcolor = (255, 255, 255)
# 字体颜色，默认为蓝色
fontcolor = (0, 0, 255)
# 干扰线颜色。默认为红色
linecolor = (255, 0, 0)
# 是否要加入干扰线
draw_line = True
# 加入干扰线条数的上下限
line_number = (1, 5)


# 原来生成字符串
def gene_text(randomlength=4):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    rand = Random()
    for i in range(randomlength):
        str += chars[rand.randint(0, length)]
    return str.upper()


# 用来绘制干扰线
def gene_line(draw, width, height):
    begin = (random.randint(0, width), random.randint(0, height))
    end = (random.randint(0, width), random.randint(0, height))
    draw.line([begin, end], fill=linecolor)


# 生成验证码
def gene_code(filename):
    width, height = size  # 宽和高
    image = Image.new('RGBA', (width, height), bgcolor)  # 创建图片
    font = ImageFont.truetype(font_path, 25)  # 验证码的字体
    draw = ImageDraw.Draw(image)  # 创建画笔
    text = gene_text()  # 生成字符串
    font_width, font_height = font.getsize(text)
    draw.text(((width - font_width) / number, (height - font_height) / number), text,
              font=font, fill=fontcolor)  # 填充字符串
    if draw_line:
        gene_line(draw, width, height)
    image = image.transform((width + 20, height + 10), Image.AFFINE, (1, -0.3, 0, -0.1, 1, 0), Image.BILINEAR)  # 创建扭曲
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)  # 滤镜，边界加强
    image.save('D:/BaiduNetdiskDownload/FlaskMooc/app/static/chapter/{}.png'.format(filename))  # 保存验证码图片
    return '{}'.format(filename)


if __name__ == "__main__":
    gene_code("77")
