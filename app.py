from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from flask_restful import Api, Resource
from farm.Farm import skitfarmPub, skitfarmSub

app = Flask(__name__)
CORS(app)
api = Api(app)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "kenya covid cases"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

api.add_resource(skitfarmPub, '/publish')
api.add_resource(skitfarmSub, '/subscribe')

if __name__ == '__main__':
    app.run()
