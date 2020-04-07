# Local Testing

## To run only this micro-service
```shell script
docker-compose up -d
docker-compose down -v --rmi='all'
```

## Test locally

```shell script
http://localhost:8081/api/docs/
```

## Initialize the DB
```shell script
curl -X POST -F 'image=banana.png' -F 'name=Product 1' -F 'price=2' -F 'slug=product-1' http://localhost:8081/api/product/create 
curl -X POST -F 'image=coffee.png' -F 'name=Coffee' -F 'price=5' -F 'slug=product-2' http://localhost:8081/api/product/create 
curl -X POST -F 'image=rubber_duck.png' -F 'name=Rubber Duck' -F 'price=2' -F 'slug=product-3' http://localhost:8081/api/product/create 
```

## Virtual Environment

```shell script
cd product-service
source vevn/bin/activate
pip install -r app/requirements.txt
```

Use "$ deactivate" when you are done.