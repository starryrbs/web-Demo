from . import *
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

# 上传文件
def uploadFile():
    pass

# 下载文件
def downloadFile():
    pass

# 取消上传的文件
def cancelfile():
    pass

# 查看文件信息(包括文件名,被下载次数,上传人,评论信息)
def showfile():
    pass

# 评论资源功能
def commentFile():
   pass

# 添加收藏
def addCollect():
    pass

# 取消收藏
def cancelCollect():
    pass

# 检测文件重复(根据标题)
def detectionRepetition():
    pass