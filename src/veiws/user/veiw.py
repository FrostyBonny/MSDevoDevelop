from flask_restful import Api, Resource, url_for, abort
from . import user
# from .parser import putPaeser, getParser
from . import parser as allParser
# from ... import dbclient
from src import dbclient
from flask import jsonify,request
from utils.code import Code
from utils.function import make_result, make_token, verify_token

table = 'my_users'
api = Api(user)
class Login(Resource):
    #  登录
    def post(self):
        args = allParser.postLoginParser.parse_args()
        m_user = dbclient.list_one(table,{"username":args["username"]})
        if m_user['password'] == args['password']:
            token = make_token()
            dbclient.update(table,token,{"username":args["username"]})
            response = make_result(data=token,code=Code.SUCCESS)
        else:
            response = make_result(code=Code.ERROR)
        return response

api.add_resource(Login, '/login',endpoint='userLogin')

class User(Resource):
    def get(self):
        args = allParser.getUserParser.parse_args()
        verify_result = verify_token(args["token"])
        if not verify_result:
            return make_result(code=Code.ERROR)
        args.pop('token')
        if 'username' in args.keys():
            m_result = dbclient.list_one(table,{"username":args["username"]})
            if not m_result:
                return make_result(code=Code.ERROR)
            m_result.pop('endtime')
            m_result.pop('token')
            if m_result:
                response = make_result(m_result,code=Code.SUCCESS)
        elif 'id' in args.keys():
            m_result = dbclient.list_one(table,{"id":args["id"]})
            if not m_result:
                return make_result(code=Code.ERROR)
            m_result.pop('endtime')
            m_result.pop('token')
            if m_result:
                response = make_result(m_result,code=Code.SUCCESS)
        return response


    def post(self):
        args = allParser.postUserParser.parse_args()
        verify_result = verify_token(args["token"])
        if not verify_result:
            return make_result(code=Code.ERROR)
        args.pop('token')
        values_keys = ['username','password']
        condition_keys = ['id']
        values = {key: value for key, value in args.items() if key in values_keys and args[key]}
        condition = {key: value for key, value in args.items() if key in condition_keys}
        m_result = dbclient.update(table,values,condition)
        if m_result:
            response = make_result(code=Code.SUCCESS)
        return response


    def delete(self):
        args = allParser.deleteUserParser.parse_args()
        verify_result = verify_token(args["token"])
        if not verify_result:
            return make_result(code=Code.ERROR)
        args.pop('token')
        m_result = dbclient.delete(table,args)
        if m_result:
            response = make_result(code=Code.SUCCESS)
        else:
            response = make_result(code=Code.ERROR)
        return response


    def put(self):
        args = allParser.putUserParser.parse_args()
        m_users = dbclient.list_column(table,['username'])
        if args['username'] in m_users:
            return make_result(code=Code.ERROR)
        m_result = dbclient.insert(table,args)
        if m_result:
            response = make_result(code=Code.SUCCESS)
        else:
            response = make_result(code=Code.ERROR)
        return response
    

api.add_resource(User, '/user',endpoint='user')