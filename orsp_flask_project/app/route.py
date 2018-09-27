from app.app import app

from flask import redirect, url_for, request,render_template,jsonify,make_response

from .route_user import user_app
from .route_file import file_app
from .route_goods import goods_app


# 首页
@app.route('/')
def index():
    pass

# 测试
@app.route('/test',methods=['GET','POST'])
def test():
    pass



app.register_blueprint(user_app, url_prefix='/user')
app.register_blueprint(file_app, url_prefix='/file')
app.register_blueprint(goods_app, url_prefix='/goods')






