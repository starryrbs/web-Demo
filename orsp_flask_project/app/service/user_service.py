from app.dao import user_dao
from werkzeug.security import generate_password_hash, check_password_hash
import re
from flask import request
from app.utils.util_token import jwtEncoding
# 用户登录
def login():
    pass

# 用户注册
def register(request):
    telephone=request.json["telephone"]
    password=request.json["password"]
    username = request.json["username"]
    code = {}
    # 对telephone和password进行判断,防止postman类似的工具
    if str(telephone).isdigit() and len(telephone)==11:
        # 对密码进行加密
        password = generate_password_hash(password, method='pbkdf2:sha1:2000', salt_length=8)
        user={
            "telephone":telephone,
            "password":password,
            "username":username
        }
        token=jwtEncoding(user)
        res=user_dao.register(user)
        print("token",token)
        if res==1:
            code["status"]="success"
            code["token"]=token.decode()
        else:

            code["status"] = "fail"
    else:
        code["status"] = "fail"
    return code

# 判断用户是否存在
def isExist(request):
    print(request.values["telephone"])
    telephone=request.values["telephone"]

    res=user_dao.isExist(telephone)
    code={}
    if res==1:
        code["status"]="exist"
    else:
        code["status"]="not exist"
    return code
#修改密码
def changePsd():
    pass

# 上传头像 是一个 url地址+图片名字
def uploadIcon():
    pass

# 用户上传文件
def uploadFile():
    pass

# 用户下载文件
def downloadFile():
    pass

# 用户查看积分,头像,名称,等基本信息
def showUser():
    pass

# 给管理员留言功能
def leaveWord():
    pass

# 花钱购买积分
def buyIntegral():
    pass