import setup
import logging
import os

app = setup.create_app()

log_name = 'product-service.log'
path = os.getenv('LOG_PATH')
if path:
    path = path + log_name
else:
    path = log_name
logging.basicConfig(filename=path, level=logging.DEBUG)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
