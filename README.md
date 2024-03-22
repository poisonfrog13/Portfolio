# My Portfolio Website

## Deployment
Start by cloning the code to the server.
```
```

Next, configure your environment variables.
```
cp env/production/django.env.example env/production/django.env
cp env/production/nginx-certbot.env.example env/production/nginx-certbot.env
```


Then you are ready to spin up your containers. Firstly you will need to login to the docker registry to get access to the certbot image. 
```
docker login -u <username>              # Then provide your PAT

docker-compose up -d --build
```





## Running Django in production
```
docker build -t django-app:1.0 .

docker run --env-file -d -p 8003:8002 django-app:1.0
```

## Running Nginx in production
```
docker build -t portfolio-nginx nginx/

docker run --name ngx -d -p 8004:80 portfolio-nginx
```

## Running the containers with docker-compose
```
docker-compose up -d 

# or in order to rebuild the images firstly

docker-compose up -d --build

docker-compose down

```

