from flask_restful import Api, Resource, url_for
from . import classRoom

api = Api(classRoom)
class ClassRoom(Resource):
    def get(self, id):
        return {'task': 'Say "Hello, World!"'}

api.add_resource(ClassRoom, '/todos/<int:id>')