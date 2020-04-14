import logging.config
import os
import settings
from flask import Flask
from gateway_api import gateway_api_blueprint
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)

app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME

app.register_blueprint(gateway_api_blueprint)

swaggerui_blueprint = get_swaggerui_blueprint(
    settings.SWAGGER_URL,
    settings.API_URL,
)
app.register_blueprint(swaggerui_blueprint, url_prefix=settings.SWAGGER_URL)

if __name__ == '__main__':
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=settings.FLASK_DEBUG)
