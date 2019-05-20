from flask_restful import Api, Resource, url_for, abort
from . import sc
# from .parser import putPaeser, getParser
from . import parser as allParser
from ... import dbclient
from flask import jsonify, request
from utils.code import Code
from utils.function import make_result, verify_token, pagenation, dbclient_decorate

table = 'sc'
api = Api(sc)
class SC(Resource):
    #  获取数据
    @dbclient_decorate
    def get(self):
        args = allParser.getParser.parse_args()
        verify_result = verify_token(args["token"])
        if not verify_result:
            return make_result(code=Code.ERROR,msg="token失效")
        args.pop('token')
        if args["type"] == "all":
            data = dbclient.list_all(table)
            length = len(data)
            data = pagenation(data,args["page"] - 1,args["limit"])
            if data:
                response = make_result(data,Code.SUCCESS,count=length)
            elif data == False:
                response = make_result(code=Code.ERROR,msg='获取数据失败')
            return response
        else:
            if args['id']:
                data = dbclient.list_one(table,{"id":args['id']})
                
                data = data[0]
                if not data:
                    return make_result(data,Code.ERROR,msg='查询失败或者没有信息')                    
            elif args['student']:
                data = dbclient.list_one(table,{"student":args['student']})
                if len(data) == 0:
                    return make_result(data,Code.ERROR,msg='查询失败或者没有信息')
            return make_result(data,Code.SUCCESS,msg='成功')
            
        # print(len(data))
        
    
    #  新增数据
    @dbclient_decorate
    def put(self):
        args = allParser.putParser.parse_args()
        verify_result = verify_token(args["token"])
        if not verify_result:
            return make_result(code=Code.ERROR)
        args.pop('token')
        result = dbclient.insert(table,args)
        if result:
            response = make_result(code=Code.SUCCESS, msg='新增成功')
        else:
            response = make_result(code=Code.ERROR, msg='新增失败')
        return response

    #  更新数据
    @dbclient_decorate
    def post(self):
        args = allParser.postParser.parse_args()
        if args.id == None:
            _t = str(request.get_data(), encoding = "utf-8")
            _t = _t.split("&")
            for i in _t:
                _l = i.split("=")
                args[_l[0]] = _l[1]
        verify_result = verify_token(args["token"])
        if not verify_result:
            return make_result(code=Code.ERROR,msg="token失效")
        args.pop('token')
        for i in list(args.keys()):
            if args[i] == None:
                del args[i]
        result = dbclient.update(table,args,{"id":args["id"]})
        if result:
            response = make_result(code=Code.SUCCESS)
        else:
            response = make_result(code=Code.ERROR,msg="修改失败")
        return response
        return make_response(jsonify({"test":"Ttest"}))

    
    #  删除数据
    @dbclient_decorate
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
            response = make_result(code=Code.ERROR,msg='删除失败')
        return response

api.add_resource(SC, '/',endpoint='SC')


