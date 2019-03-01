from .code import Code
from flask import jsonify, make_response

def create_insert_sql(values):
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
    jsonData = jsonify({"code": code, "data": data, "msg": Code.msg[code]})
    response = make_response(jsonData)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response