from flask_restful import Api, Resource, url_for, abort
from . import classRoom
# from .parser import putPaeser, getParser
from . import parser as allParser
from ... import dbclient
from flask import jsonify
from utils.code import Code
from utils.function import make_result

table = 'classRoom'
api = Api(classRoom)
class ClassRoom(Resource):
    #  获取数据
    def get(self):
        # print()
        args = allParser.getParser.parse_args()
        verify_result = verify_token(args["token"])
        if not verify_result:
            return make_result(code=Code.ERROR)
        args.pop('token')
        if args["type"] == "all":
            data = dbclient.list_all(table)
        else:
            data = dbclient.list_one(table,{"id":args['id']})
        if data is None:
            response = make_result(data,Code.SUCCESS)
        elif data == False:
            response = make_result(code=Code.ERROR)
        return response
    
    #  更新数据
    def put(self):
        args = allParser.putParser.parse_args()
        verify_result = verify_token(args["token"])
        if not verify_result:
            return make_result(code=Code.ERROR)
        args.pop('token')
        result = dbclient.update(table,args,{"id":args["id"]})
        if result:
            response = make_result(code=Code.SUCCESS)
        else:
            response = make_result(code=Code.ERROR)
        return response
        # return make_response(jsonify({"test":"Ttest"}))

    #  新增数据
    def post(self):
        args = allParser.postParser.parse_args()
        verify_result = verify_token(args["token"])
        if not verify_result:
            return make_result(code=Code.ERROR)
        args.pop('token')
        result = dbclient.insert(table,args)
        if result:
            response = make_result(code=Code.SUCCESS)
        else:
            response = make_result(code=Code.ERROR)
        return response

    
    #  删除数据
    def delete(self):
        args = allParser.deleteParser.parse_args()
        verify_result = verify_token(args["token"])
        if not verify_result:
            return make_result(code=Code.ERROR)
        args.pop('token')
        result = dbclient.delete(table,{"id":args['id']})
        if result:
            response = make_result(code=Code.SUCCESS)
        else:
            response = make_result(code=Code.ERROR)
        return response

api.add_resource(ClassRoom, '/',endpoint='classRoom')


