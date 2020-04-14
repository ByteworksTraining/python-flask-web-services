import logging.config
import os
import settings
from flask import Flask, jsonify, make_response
from gateway_api import gateway_api_blueprint
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)

app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
app.config['USER_CLIENT_URL'] = settings.USER_CLIENT_URL

app.register_blueprint(gateway_api_blueprint)

### swagger specific ###
swaggerui_blueprint = get_swaggerui_blueprint(
    settings.SWAGGER_URL,
    settings.API_URL,
    config={
        'app_name': 'API Gateway'
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=settings.SWAGGER_URL)
### end swagger specific ###

@app.errorhandler(400)
def handle_400_error(_error):
    """Return a http 400 error to client"""
    return make_response(jsonify({'error': 'Misunderstood'}), 400)


@app.errorhandler(401)
def handle_401_error(_error):
    """Return a http 401 error to client"""
    return make_response(jsonify({'error': 'Unauthorised'}), 401)


@app.errorhandler(404)
def handle_404_error(_error):
    """Return a http 404 error to client"""
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(500)
def handle_500_error(_error):
    """Return a http 500 error to client"""
    return make_response(jsonify({'error': 'Server error'}), 500)


if __name__ == '__main__':
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=settings.FLASK_DEBUG)
