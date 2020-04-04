from flask import Flask
from product_api import product_api_blueprint
from flask_swagger_ui import get_swaggerui_blueprint
import models
import logging

SWAGGER_URL = '/api/docs'
API_URL = '/api/product/docs.json'


def create_app():
    logging.debug('create_app()')
    app = Flask(__name__)

    app.config.update({'SECRET_KEY': "powerful secretkey", 'WTF_CSRF_SECRET_KEY': "a csrf secret key",
                       'SQLALCHEMY_DATABASE_URI': 'mysql+mysqlconnector://root:test@product_db/product',
                       'SQLALCHEMY_TRACK_MODIFICATIONS': False})

    models.init_app(app)
    models.create_tables(app)

    app.register_blueprint(product_api_blueprint)

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app
