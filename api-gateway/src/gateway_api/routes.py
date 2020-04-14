import logging
from flask import make_response, request, json, jsonify, abort
from . import gateway_api_blueprint
from .services.user_client import UserClient


@gateway_api_blueprint.route('/api/gateway/version')
def get_version():
    return {'version': "1.0.0"}


@gateway_api_blueprint.route('/api/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if not username:
        return make_response("Username parameter is missing", 400)
    if not password:
        return make_response("Password parameter is missing", 400)
    payload = {
        'username': username,
        'password': password,
    }
    return UserClient.post_login(payload)
