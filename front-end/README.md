# Packt Hands on Microservices with Python

Author: Peter Fisher

# Installation
- Read the [requirements](docs/install/requirements.md) guide first
- To install the whole application read the [Microservices installation guide](docs/install/microservices.md)
- To install just the frontend read the [Frontend installation guide](docs/install/frontend.md)


## To Run only the Front End
```shell script
docker-compose up -d
docker-compose down -v --rmi='all'
```

## To run all services
```shell script
docker-compose -f docker-compose.deploy.yml up -d
docker-compose down -v --rmi='all'

```


* Front End - http://localhost/
  1) Register a new user
  2) Login
* Product API - http://localhost:8081/api/docs/
* User API - http://localhost:8082/api/docs/
* Order API - http://localhost:8083/api/docs/
 