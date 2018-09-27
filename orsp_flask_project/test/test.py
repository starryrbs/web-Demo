# Author:raobaoshi
# from werkzeug.security import generate_password_hash, check_password_hash
# password="123"
# res=generate_password_hash(password, method='pbkdf2:sha1:2000', salt_length=8)
# print(res)
#
# dat=check_password_hash(res, password)
# print(dat)
import re
str="Duplicate entry '15755407860' for key 'tel_unqiue'"

print(re.findall(r'tel_unqiue',str))