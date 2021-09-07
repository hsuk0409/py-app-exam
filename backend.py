import flask
import flask_restful
from flask_restful import reqparse

app = flask.Flask(__name__)
api = flask_restful.Api(app)


def multiply(x, y) -> int:
    return x * y


class HelloWorld(flask_restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()

        parser.add_argument('param1')
        parser.add_argument('param2')
        args = parser.parse_args()

        param1 = args['param1']
        param2 = args['param2']

        if (not param1) or (not param2):
            return {
                'state': 0,
                'response': None
            }

        param1 = int(param1)
        param2 = int(param2)

        result = multiply(param1, param2)

        return {
            'state': 1,
            'response': result
        }


api.add_resource(HelloWorld, '/api/multiply')

if __name__ == '__main__':
    app.run()
