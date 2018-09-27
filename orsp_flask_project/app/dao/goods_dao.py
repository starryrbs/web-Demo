from app.dao.__init__ import *
from app.dao.sql_file.goods_sql import do_goods_sql
'''
cursorclass = MySQLdb.cursors.DictCursor
 
'''


# 连接数据库模块
def test(user):
    try:
        res=0
        connect=creatConnect()
        cursor = connect.cursor(pymysql.cursors.DictCursor)
        sql=do_goods_sql['get_product_type_one']
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




# 获取一级商品类型
def get_product_type_one():
    try:
        res=0
        cursor=None
        connect=None
        connect=creatConnect()
        cursor = connect.cursor(pymysql.cursors.DictCursor)
        sql=do_goods_sql['get_product_type_one']
        res = cursor.execute(sql)
        data=cursor.fetchall()
        connect.commit()
    except Exception as ex:
        print(ex)
        return 0
    finally:
        if cursor:
            cursor.close()
        if connect:
            connect.close()
    return data
# 获取二级商品类型
def get_product_type_two(id):
    try:
        res=0
        cursor=None
        connect=None
        connect=creatConnect()
        cursor = connect.cursor(pymysql.cursors.DictCursor)
        sql=do_goods_sql['get_product_type_two'].format(id)
        res = cursor.execute(sql)
        data=cursor.fetchall()
        connect.commit()
    except Exception as ex:
        print(ex)
        return 0
    finally:
        if cursor:
            cursor.close()
        if connect:
            connect.close()
    return data
# 获取三级商品类型
def get_product_type_three(id):
    try:
        res=0
        cursor=None
        connect=None
        connect=creatConnect()
        cursor = connect.cursor(pymysql.cursors.DictCursor)
        sql=do_goods_sql['get_product_type_three'].format(id)
        res = cursor.execute(sql)
        data=cursor.fetchall()
        connect.commit()
    except Exception as ex:
        print(ex)
        return 0
    finally:
        if cursor:
            cursor.close()
        if connect:
            connect.close()
    return data
# 添加收藏
def addCollect():
    pass

#取消收藏
def cancelCollect():
    pass

# 上传商品
def uploadGoods():
    pass

# 下架商品
def downloadGoods():
    pass

# 生成订单
def generateOrder():
    pass

# 查看商品详情
def showGoods():
    pass

# 评论商品
def commentGoods():
    pass