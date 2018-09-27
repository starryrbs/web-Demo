from flask import Blueprint, request, make_response, session, render_template, redirect, json
from datetime import timedelta, datetime
from app.utils.util_token import *
from app.service.user_service import *

# 用参数name和import_name初始化
file_app = Blueprint('file', __name__)

# 上传文件
@file_app.route('/uploadfile')
def uploadFile():
    pass

# 下载文件
@file_app.route('/downloadfile')
def downloadFile():
    pass

# 取消上传的文件
@file_app.route('/cancelfile')
def cancelfile():
    pass

# 查看文件信息(包括文件名,被下载次数,上传人,评论信息)
@file_app.route('/showfile')
def showfile():
    pass

# 评论资源功能
@file_app.route('/commentfile')
def commentFile():
   pass

# 添加收藏
@file_app.route('/addcollect')
def addCollect():
    pass

# 取消收藏
@file_app.route('/cancelcollect')
def cancelCollect():
    pass

# 检测文件重复(根据标题)
@file_app.route('/detectionrepetition')
def detectionRepetition():
    pass