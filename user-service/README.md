# Local Testing

## Deploy locally
```shell script
docker-compose up
```

## Test locally

```shell script
http://localhost:8082/api/docs/
```

## Virtual Environment

While you should be able to set-up the virtual environment for each microservice from the command line with "python -m venv...", I didn't have luck with that.
Instead, you can do it from the ide, like PyCharm:

![venv](https://github.com/smitchell/python-flask-web-services/raw/master/AddPythonVirtualEnvironment.png)

Activate the environment and install the requirements:

```shell script
cd user-service
source vevn/bin/activate
pip install -r app/requirements.txt
```

Use "$ deactivate" when you are done.