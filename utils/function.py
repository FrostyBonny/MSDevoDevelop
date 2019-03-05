from .code import Code
from flask import jsonify, make_response
import string
import random
import src
import time


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

def make_result(data=None, code=Code.SUCCESS):
    if not isinstance(data,dict) and data != None:
        raise TypeError('data must be dict')
    jsonData = jsonify({"code": code, "data": data, "msg": Code.msg[code]})
    response = make_response(jsonData)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


def make_token():
    result = {}
    result['token'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    return result


def verify_token(token):
    m_result = src.dbclient.list_one('my_users',{"token":token})
    if m_result:
        current_time = int(time.time())
        token_end_time = int(time.mktime(time.strptime(str(m_result['endtime']), "%Y-%m-%d %H:%M:%S")))
        # print(current_time,token_end_time)
        # 此处报错
        differ = current_time - token
        if 0 < differ and differ < 7200:
            return True
        else:
            return False
    else:
        return False
