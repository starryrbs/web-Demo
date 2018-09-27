from flask import Flask,session
# 解决跨域的第二种方案
import flask_cors

app=Flask(__name__)
# supports_credentials=True可以让特殊的情况也跨域：header,上传文件,put,delete
flask_cors.CORS(app, supports_credentials=True)
app.config.from_object('app.conf')


