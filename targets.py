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
        print("Getting")
        print(TARGETS)
        return TARGETS

    def post(self):
        request.get_json(force=True)
        args = parser.parse_args()

        TARGETS['targets'] = args['targets']

        print("Args")
        print(args)
        print("TARGETS")
        print(TARGETS)

        return TARGETS


##
## Actually setup the Api resource routing here
##
api.add_resource(Targets, '/')

if __name__ == '__main__':
    app.run(debug=True)
