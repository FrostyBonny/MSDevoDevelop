from flask_restful import Api, Resource, url_for, abort
from . import user
# from .parser import putPaeser, getParser
from . import parser as allParser
# from ... import dbclient
from src import dbclient
from flask import jsonify,request
from utils.code import Code
from utils.function import make_result, make_token, verify_token, encode_password

table = 'my_users'
api = Api(user)
class Login(Resource):
    #  登录
    def post(self):
        args = allParser.postLoginParser.parse_args()
        m_user = dbclient.list_one(table,{"username":args["username"]})
        if not m_user:
            return make_result(code=Code.ERROR, msg="没有该用户")
        m_user = m_user[0]        
        if m_user['password'] == encode_password(args['password']):
            token = make_token()
            dbclient.update(table,token,{"username":args["username"]})
            # token["username"]
            back = {}
            back["name"] = m_user["name"]
            back["token"] = token["token"]
            back["role"] = m_user["role"]
            response = make_result(data=back,code=Code.SUCCESS)
        else:
            response = make_result(code=Code.ERROR, msg="账户密码不一致")
        return response
    
    def get(self):
        args = allParser.getLoginParser.parse_args()
        verify_result = verify_token(args["token"])
        if not verify_result:
            return make_result(code=Code.ERROR, msg="token无效")
        else:
            return make_result(code=Code.SUCCESS, msg="成功")



api.add_resource(Login, '/login',endpoint='userLogin')

class Login_Out(Resource):
    def post(self):
        args = allParser.getLoginOutParser.parse_args()
        verify_result = verify_token(args["token"])
        if not verify_result:
            return make_result(code=Code.SUCCESS, msg="token已失效")
        else:
            new_token = make_token()
            result = dbclient.update(table,new_token,{"token":args["token"]})
            if result:
                return make_result(code=Code.SUCCESS)
            else:
                return make_result(code=Code.ERROR,msg="登出失败")

api.add_resource(Login_Out, '/loginout',endpoint='userLoginOut')

class User(Resource):
    #  获取
    def get(self):
        args = allParser.getUserParser.parse_args()
        verify_result = verify_token(args["token"])
        if not verify_result:
            return make_result(code=Code.ERROR, msg="token错误")
        args.pop('token')
        if args['type'] == 'all':
            m_result = dbclient.list_all(table)
            if not m_result:
                return make_result(code=Code.ERROR, msg="查询错误")
            for index,i in enumerate(m_result):
                m_result[index] = {
                    "id":i["id"],
                    "username":i["username"],
                    "name":i['name'],
                    "role":i['role'],
                }
            response = make_result(m_result,code=Code.SUCCESS)
        else:
            if 'username' in args.keys():
                m_result = dbclient.list_one(table,{"username":args["username"]})
                if not m_result:
                    return make_result(code=Code.ERROR, msg="没有该用户")
                m_result[0].pop('endtime')
                m_result[0].pop('token')
                response = make_result(m_result,code=Code.SUCCESS)
            elif 'id' in args.keys():
                m_result = dbclient.list_one(table,{"id":args["id"]})
                m_result = m_result[0]
                if not m_result:
                    return make_result(code=Code.ERROR, msg="没有该用户")
                m_result[0].pop('endtime')
                m_result[0].pop('token')
                response = make_result(m_result,code=Code.SUCCESS)
        return response


    #  更新
    def post(self):
        args = allParser.postUserParser.parse_args()
        verify_result = verify_token(args["token"])
        if not verify_result:
            return make_result(code=Code.ERROR, msg="token无效")
        args.pop('token')
        values_keys = ['username','password','name','role']
        condition_keys = ['id']
        values = {key: value for key, value in args.items() if key in values_keys and args[key]}
        condition = {key: value for key, value in args.items() if key in condition_keys}
        values["password"] = encode_password(values["password"])
        m_result = dbclient.update(table,values,condition)
        if m_result:
            response = make_result(code=Code.SUCCESS)
        else:
            response = make_result(code=Code.ERROR, msg="更新失败")
        return response


    #  删除
    def delete(self):
        args = allParser.deleteUserParser.parse_args()
        verify_result = verify_token(args["token"])
        if not verify_result:
            return make_result(code=Code.ERROR, msg="token无效")
        args.pop('token')
        m_result = dbclient.delete(table,args)
        if m_result:
            response = make_result(code=Code.SUCCESS)
        else:
            response = make_result(code=Code.ERROR, msg="删除失败")
        return response


    #  新增
    def put(self):
        args = allParser.putUserParser.parse_args()
        m_users = dbclient.list_column(table,['username'])
        if args['username'] in m_users:
            return make_result(code=Code.ERROR, msg="已经存在此用户")
        args["password"] = encode_password(args["password"])
        m_result = dbclient.insert(table,args)
        if m_result:
            response = make_result(code=Code.SUCCESS)
        else:
            response = make_result(code=Code.ERROR, msg="新增失败")
        return response
    

api.add_resource(User, '/user',endpoint='user')