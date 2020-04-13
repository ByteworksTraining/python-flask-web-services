import logging
import os
from flask import make_response, request, json, jsonify, abort
from . import gateway_api_blueprint


@gateway_api_blueprint.route('/api/gateway/docs.json', methods=['GET'])
def swagger_api_docs_yml():
    logging.debug('swagger_api_docs_yml()')
    current_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(current_path, "../swagger.json")
    with open(path) as fd:
        json_data = json.load(fd)

    return jsonify(json_data)


@gateway_api_blueprint.route('/api/gateway/version')
def get_version():
    return {'version': 1.0}
