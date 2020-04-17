import os
import flask

from flask import Flask
from flask_classful import FlaskView, route

app = Flask(__name__)


class FlaskClassfulEx(FlaskView):

    @route('/')
    def hello_world(self):
       target = os.environ.get('TARGET', 'World')
       return 'Hello {}!\n'.format(target)

FlaskClassfulEx.register(app, route_base='/')


# @app.route('/')
# def hello_world():
#    target = os.environ.get('TARGET', 'World')
#    return 'Hello {}!\n'.format(target)

if __name__ == "__main__":
    
    with app.test_request_context():
        print(flask.url_for("FlaskClassfulEx:hello_world"))

    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
