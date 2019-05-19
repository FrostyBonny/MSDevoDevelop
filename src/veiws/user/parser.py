from flask_restful import reqparse

getUserParser = reqparse.RequestParser()
getUserParser.add_argument('id', type=int, help='please enter id')
getUserParser.add_argument('username', type=str, help='please enter username')
getUserParser.add_argument('type', type=str, help='please enter type')
getUserParser.add_argument('token', type=str, location='headers')
getUserParser.add_argument('page', type=int, help='please enter page')
getUserParser.add_argument('limit', type=int, help='please enter limit')

deleteUserParser = reqparse.RequestParser()
deleteUserParser.add_argument('id', type=int, help='please enter id', required=True)
deleteUserParser.add_argument('token', type=str, location='headers')


putUserParser = reqparse.RequestParser()
putUserParser.add_argument('username', type=str, help='please enter username', required=True)
putUserParser.add_argument('password', type=str, help='please enter password', required=True)
putUserParser.add_argument('role', type=str, help='please enter role', required=True)
putUserParser.add_argument('name', type=str, help='please enter name', required=True)
putUserParser.add_argument('class', type=str, help='please enter name', required=True)
putUserParser.add_argument('phone', type=str, help='please enter name', required=True)



postUserParser = reqparse.RequestParser()
postUserParser.add_argument('id', type=str, help='please enter id', required=True)
postUserParser.add_argument('username', type=str, help='please enter username', required=True)
postUserParser.add_argument('role', type=str, help='please enter role', required=True)
postUserParser.add_argument('name', type=str, help='please enter name', required=True)
postUserParser.add_argument('password', type=str, help='please enter password', required=True)
postUserParser.add_argument('phone', type=str, help='please enter phone', required=True)
postUserParser.add_argument('token', type=str, location='headers')


postLoginParser = reqparse.RequestParser()
postLoginParser.add_argument('username', type=str, help='please enter username', required=True)
postLoginParser.add_argument('password', type=str, help='please enter password', required=True)

getLoginParser = reqparse.RequestParser()
getLoginParser.add_argument('token', type=str, location='headers')

getLoginOutParser = reqparse.RequestParser()
getLoginOutParser.add_argument('token', type=str, location='headers')

# args = parser.parse_args()