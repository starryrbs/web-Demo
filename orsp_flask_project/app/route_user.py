from flask import Blueprint, request, make_response, session, render_template, redirect, json
from datetime import timedelta, datetime
from app.utils.util_token import *
from app.service import user_service

# 用参数name和import_name初始化
user_app = Blueprint('user', __name__)

# 用户登录
@user_app.route('/login',methods=["POST"])
def login():
    pass

# 验证用户是否已存在
@user_app.route('/isexist')  # /user/add
def isExist():
    print("111111111")
    res=user_service.isExist(request)
    print("res",res)
    return json.dumps(res)
# 用户注册
@user_app.route('/register',methods=["POST"])  # /user/add
def register():
    res=user_service.register(request)
    print("res",res)
    print(type(res))
    print(json.dumps(res))
    return json.dumps(res)

#修改密码
@user_app.route('/changepsd',methods=['POST'])
def changePsd():
    pass

# 上传头像 是一个 url地址+图片名字
@user_app.route('/uploadicon')
def uploadIcon():
    pass

# 用户上传文件
@user_app.route('/uploadfile')  # /user/show
def uploadFile():
    pass

# 用户下载文件
@user_app.route('/downloadfile')
def downloadFile():
    pass

# 用户查看积分,头像,名称,等基本信息
@user_app.route('/showuser')
def showUser():
    pass

# 给管理员留言功能
@user_app.route('/leaveword')
def leaveWord():
    pass

# 花钱购买积分
@user_app.route('/buyintegral')
def buyIntegral():
    pass