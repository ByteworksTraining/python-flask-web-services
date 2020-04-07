# Local Testing

## To run only this micro-service
```shell script
docker-compose up -d
docker-compose down -v --rmi='all'
```

## Test locally

```shell script
http://localhost:8083/api/docs/
```

## Virtual Environment

```shell script
cd order-service
source vevn/bin/activate
pip install -r app/requirements.txt
```

Use "$ deactivate" when you are done.