This project is based on [Hands-on Microscervice by Peter Fisher](https://github.com/smitchell/python-flask-web-services)
I am building on top of Peter's code to create my personal referencing implementation liek what I am used to with Spring Cloud.
As with Peter's project, this is not meant to be production quality code, but rather it is a test bed for microservice concepts.

# Docker

To run this project with Docker change to the front-end and follow the instructions in front-end/README.md.


# Virtual Environments

Setup a virtual environment for each service.

## Front End

```shell script
cd front-end
python3 -m venv venv
source venv/bin/activate
pip install -r app/requirements.txt
deactivate
cd ..
```

## Order Service

```shell script
cd order-service
python3 -m venv venv
source venv/bin/activate
pip install -r app/requirements.txt
deactivate
cd ..
```

## Product Service

```shell script
cd product-service
python3 -m venv venv
source venv/bin/activate
pip install -r app/requirements.txt
deactivate
cd ..
```

## User Service

```shell script
cd user-service
python3 -m venv venv
source venv/bin/activate
pip install -r app/requirements.txt
deactivate
cd ..
```
