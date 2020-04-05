
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