from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('targets', type=list, location='json')


TARGETS = {
        "targets": [ 1, 2, 3 ] 
}

class Targets(Resource):
    def get(self):
        return TARGETS

    def post(self):
        request.get_json(force=True)
        args = parser.parse_args()

        TARGETS['targets'] = args['targets']

        return TARGETS


##
## Actually setup the Api resource routing here
##
api.add_resource(Targets, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
