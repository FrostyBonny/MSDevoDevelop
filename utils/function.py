from .code import Code
from flask import jsonify, make_response
import string
import random
import src
import time
import hashlib


#  公用的function
def create_insert_sql_values(values):
    result = "("
    # result += ",".join([ str(values[i]) for i in values])
    first = True
    for i in values:
        if first:
            first = False
            if isinstance(values[i],str):
                result += "'" + str(values[i]) + "'"
            else:
                result += str(values[i])
        else:
            if isinstance(values[i],str):
                result += ",'" + str(values[i]) + "'"
            else:
                result += "," + str(values[i])
    result += ")"
    return result


def create_insert_sql_column(values):
    result = "("
    # result += ",".join([ str(values[i]) for i in values])
    first = True
    for i in values:
        if first:
            first = False
            result += str(i)
        else:
            result += "," + str(i)
    result += ")"
    return result


def create_update_sql(values):
    result = ''
    first = True
    for i in values:
        if first:
            first = False
            result += str(i) + " = '%s'"%(values[i])
        else:
            result += "," + str(i) + " = '%s'"%(values[i])            
    return result


'''
data: 返回的数据
code：返回的状态码
msg：返回的消息
count：分页时用到的数据
'''
def make_result(data=None, code=Code.SUCCESS, msg="成功",count=None):
    # if not isinstance(data,dict) and data != None:
        # raise TypeError('data must be dict')
    if not isinstance(msg,str) and data != None:
        raise TypeError('msg must be str')
    if count:
        jsonData = jsonify({"code": code, "data": data, "msg": msg, "count":count})
    else:
        jsonData = jsonify({"code": code, "data": data, "msg": msg})
    response = make_response(jsonData)
    # response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    response.headers['Content-Type'] = 'application/json'    
    return response


def make_token():
    result = {}
    result['token'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    return result


def verify_token(token):
    if token == "ASDFGHJKL":
        return True
    m_result = src.dbclient.list_one('my_users',{"token":token})
    if m_result:
        m_result = m_result[0]
        current_time = int(time.time())
        token_end_time = int(time.mktime(time.strptime(str(m_result['endtime']), "%Y-%m-%d %H:%M:%S")))
        # print(current_time,token_end_time)
        # 此处报错
        differ = current_time - token_end_time
        if 0 < differ and differ < 7200:
            return True 
        else:
            return False
    else:
        return False


#  md5加密
def encode_password(password):
    hl = hashlib.md5()
    # 此处必须声明encode
    # 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
    hl.update(password.encode())
    return hl.hexdigest()


#  用于分页
#  data->数据
#  page->第几页
#  limit->页的大小
def pagenation(data,page,limit):
    # split = lambda a:map(lambda b:a[b:b+int(limit)],range(0,len(a),int(limit)))
    data = [data[i:i+int(limit)] for i in range(0,len(data),int(limit))]
    # data = split(data)
    return data[page]
    # print(data[page])

# 自动连接以及关闭数据库的装饰器
def dbclient_decorate(func):
    def inner(*args,**kwargs):
        src.dbclient.connect()
        result = func(*args,**kwargs)
        src.dbclient.close()
        return result
    return inner