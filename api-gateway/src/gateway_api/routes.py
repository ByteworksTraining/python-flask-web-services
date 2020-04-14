import logging
from flask import make_response, request, json, jsonify, abort
from . import gateway_api_blueprint
from .user_client import UserClient


@gateway_api_blueprint.route('/api/gateway/version')
def get_version():
    return {'version': "1.0.0"}


@gateway_api_blueprint.route('/api/login', methods=['POST'])
def login():
    logging.debug('login()')
    form = request.data  # data is empty
    payload = {
        'username': form.username.data,
        'password': form.password.data,
    }
    return UserClient.post_login(payload)
