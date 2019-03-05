from flask_restful import reqparse

getUserParser = reqparse.RequestParser()
getUserParser.add_argument('id', type=int, help='please enter id')
getUserParser.add_argument('username', type=int, help='please enter username')
getUserParser.add_argument('token', type=str, location='headers')

deleteUserParser = reqparse.RequestParser()
deleteUserParser.add_argument('id', type=int, help='please enter id', required=True)
deleteUserParser.add_argument('token', type=str, location='headers')


putUserParser = reqparse.RequestParser()
putUserParser.add_argument('username', type=str, help='please enter username', required=True)
putUserParser.add_argument('password', type=str, help='please enter password', required=True)


postUserParser = reqparse.RequestParser()
postUserParser.add_argument('id', type=str, help='please enter id', required=True)
postUserParser.add_argument('username', type=str, help='please enter username')
postUserParser.add_argument('password', type=str, help='please enter password')
postUserParser.add_argument('token', type=str, location='headers')


postLoginParser = reqparse.RequestParser()
postLoginParser.add_argument('username', type=str, help='please enter username', required=True)
postLoginParser.add_argument('password', type=str, help='please enter password', required=True)
# postLoginParser.add_argument('token', type=str, location='headers')

# args = parser.parse_args()