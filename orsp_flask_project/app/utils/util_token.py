import datetime
import jwt
import time
from functools import wraps
from flask import request,json

SECRET_KEY = 'com.jobapp'


# 签发token
def jwtEncoding(some, aud='webkit'):
    datetimeInt = datetime.datetime.utcnow() + datetime.timedelta(hours=10)
    option = {
        'iss': 'jobapp.com',
        'exp': datetimeInt,
        'aud': aud,
        'some': some
    }
    encoded2 = jwt.encode(option, SECRET_KEY, algorithm='HS256')
    return encoded2


# 解析jwt 信息
# def jwtDecoding(token, aud='webkit'):
#     decoded = None
#     try:
#         decoded = jwt.decode(token, SECRECT_KEY, audience=aud, algorithms=['HS256'])

#         now_time = int(time.mktime(datetime.datetime.utcnow().timetuple()))
#         if decoded['exp'] - now_time > 0:
#             return decoded
#         else:
#             decoded = None
#     except jwt.ExpiredSignatureError:
#         print("erroing.................")
#         decoded = {"error_msg": "is timeout !!", "some": None}
#     except Exception:
#         decoded = {"error_msg": "noknow exception!!", "some": None}
#         print("erroing2.................")
#     return decoded


def checkLogin(*req):
    def decorated(func):
        @wraps(func)
        def wrapper():
            # print("[DEBUG]: enter {}()".format(func.__name__))
            decoded = None
            try:
                token=request.headers['token']
                print('token is:')
                print(token)
                decoded = jwt.decode(token, SECRET_KEY, audience='webkit', algorithms=['HS256'])
                print(decoded)
            except jwt.ExpiredSignatureError:
                print("erroing.................")
                decoded = {"error_msg": "is timeout !!", "some": None}
                return json.jsonify(decoded)
            except Exception:
                decoded = {"error_msg": "noknow exception!!", "some": None}
                print("erroing2.................")
                return json.jsonify(decoded)
            return func()
        return wrapper

    return decorated
