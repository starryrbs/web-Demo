from flask import Blueprint, request, make_response, session, render_template, redirect, json
from datetime import timedelta, datetime
from app.utils.util_token import *
from app.service import goods_service

# 用参数name和import_name初始化
goods_app = Blueprint('goods', __name__)


# 获取商品类型
@goods_app.route('/getgoodtype')
def getGoodType():
    data=goods_service.getGoodType()
    return json.dumps({"result":data})
# 添加收藏
@goods_app.route('/addcollect')
def addCollect():
    pass

#取消收藏
@goods_app.route('/cancelcollect')
def cancelCollect():
    pass

# 上传商品
@goods_app.route('/uploadgoods')
def uploadGoods():
    pass

# 下架商品
@goods_app.route('/downloadgoods')
def downloadGoods():
    pass

# 生成订单
@goods_app.route('/generateorder')
def generateOrder():
    pass

# 查看商品详情
@goods_app.route('/showgoods')
def showGoods():
    pass

# 评论商品
@goods_app.route('/commentgoods')  # /user/show
def commentGoods():
    pass



