from flask_restful import reqparse

getParser = reqparse.RequestParser()
getParser.add_argument('name', type=str, help='please enter name')
getParser.add_argument('type', type=str, help='please enter type')
getParser.add_argument('page', type=int, help='please enter page')
getParser.add_argument('limit', type=int, help='please enter limit')
getParser.add_argument('token', type=str, location='headers')


deleteParser = reqparse.RequestParser()
deleteParser.add_argument('id', type=int, help='please enter id', required=True)
deleteParser.add_argument('token', type=str, location='headers')

putParser = reqparse.RequestParser()
putParser.add_argument('id', type=int, help='please enter id', required=True)
putParser.add_argument('total', type=int, help='please enter total')
putParser.add_argument('arrived', type=int, help='please enter arrived')
putParser.add_argument('name', type=str, help='please enter name')
putParser.add_argument('token', type=str, location='headers')

postParser = reqparse.RequestParser()
# postParser.add_argument('id', type=int, help='please enter id', required=True)
postParser.add_argument('name', type=str, help='please enter name')
postParser.add_argument('total', type=int, help='please enter total', required=True)
postParser.add_argument('arrived', type=int, help='please enter arrived', required=True)
postParser.add_argument('token', type=str, location='headers')
# args = parser.parse_args()