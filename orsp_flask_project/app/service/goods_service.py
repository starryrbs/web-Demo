from app.dao import goods_dao
from werkzeug.security import generate_password_hash, check_password_hash

# 查询所有商品类型

def getGoodType():
    #要返回的数据
    data=[]
    # 一级数据,为一个字典
    type_one=goods_dao.get_product_type_one()
    # print(type_one)
    # 用来计算data的下标
    index=0
    for t in type_one:
        d_one = {}
        # print(t["product_type"])
        d_one["name"]=t["product_type"]
        d_one["category"]=[]
        data.append(d_one)

        type_two=goods_dao.get_product_type_two(t["id"])
        if type(type_two)==type([]):
            # print(type_two)

            index_two = 0
            for t_t in type_two:
                d_two = {}
                d_two["name"] = t_t["type_two_name"]
                d_two["category"] = []
                # print(data)
                data[index]["category"].append(d_two)

                type_three = goods_dao.get_product_type_three(t_t["two_id"])
                print(type_three)
                # 二级data的下标
                for t_t_t in type_three:
                    # d_three = {}
                    # d_three["name"] = t_t_t["type_three_name"]
                    # print(data)
                    print(t_t_t)
                    data[index]["category"][index_two]["category"].append(t_t_t["type_three_name"])
                    print(data[index]["category"][index_two]["category"])
                index_two+=1

        index += 1
    print(data)
    return data
'''
[
    {
        name:"视频",
        category:[
        {
        name:"家居"
        category:[
        "家居建材","办公文具"
        ]
        }
        ]
    },
    {}
]

'''

# getGoodType()
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