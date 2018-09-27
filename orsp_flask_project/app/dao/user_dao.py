from app.dao.__init__ import *
from app.dao.sql_file.user_sql import do_user_sql

# 连接数据库模块
def test(user):
    try:
        res=0
        connect=creatConnect()
        cursor = connect.cursor()
        sql=do_user_sql['addUser'].format(user['telephone'],user['password'])
        res = cursor.execute(sql)
        connect.commit()
    except Exception as ex:
        print(ex)
        return 0
    finally:
        if cursor:
            cursor.close()
        if connect:
            connect.close()
    return res

# 用户登录
def login():
    pass

# 用户注册
def register(user):
    try:
        res=0
        cursor=None
        connect=None
        connect=creatConnect()
        cursor = connect.cursor()
        sql=do_user_sql['registerUser'].format(user['telephone'],user['password'],user["username"])
        res = cursor.execute(sql)
        connect.commit()
    except Exception as ex:
        print(ex)
        return ex
    finally:
        if cursor:
            cursor.close()
        if connect:
            connect.close()
    return res

# 判断用户是否存在
def isExist(telephone):
    try:
        res=0
        cursor=None
        connect=None
        connect=creatConnect()
        cursor = connect.cursor()
        sql=do_user_sql['isExist'].format(telephone)
        res = cursor.execute(sql)
        connect.commit()
    except Exception as ex:
        print(ex)
        return ex
    finally:
        if cursor:
            cursor.close()
        if connect:
            connect.close()
    return res
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