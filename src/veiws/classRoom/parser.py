from flask_restful import reqparse

getParser = reqparse.RequestParser()
getParser.add_argument('id', type=int, help='please enter id', required=True)

deleteParser = reqparse.RequestParser()
deleteParser.add_argument('id', type=int, help='please enter id', required=True)

putParser = reqparse.RequestParser()
putParser.add_argument('id', type=int, help='please enter id', required=True)
putParser.add_argument('total', type=int, help='please enter total')
putParser.add_argument('arrived', type=int, help='please enter arrived')

postParser = reqparse.RequestParser()
postParser.add_argument('id', type=int, help='please enter id', required=True)
postParser.add_argument('total', type=int, help='please enter total', required=True)
postParser.add_argument('arrived', type=int, help='please enter arrived', required=True)
# args = parser.parse_args()