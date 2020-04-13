from flask import Blueprint

gateway_api_blueprint = Blueprint('gateway_api', __name__)

from . import routes
