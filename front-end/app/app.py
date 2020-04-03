from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from frontend import frontend_blueprint
from frontend.api import UserClient

app = Flask(__name__)

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'main.login'

# TODO - Update get_user() to take an id.
@login_manager.user_loader
def load_user(user_id):
    return UserClient.get_user()

bootstrap = Bootstrap(app)


app.config.update({'SECRET_KEY': "powerful secretkey", 'WTF_CSRF_SECRET_KEY': "a csrf secret key",
                   'PRODUCT_SERVICE': 'http://192.168.1.180:8081'})

app.register_blueprint(frontend_blueprint)

app.run(debug=True, host='0.0.0.0')

