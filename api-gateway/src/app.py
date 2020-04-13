from flask import Flask
from gateway_api import gateway_api_blueprint
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

app.register_blueprint(gateway_api_blueprint)

SWAGGER_URL = '/api/docs'
API_URL = '/api/gateway/docs.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run()