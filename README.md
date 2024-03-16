## Running Django in production
```
sudo docker build -t django-app:1.0 .

sudo docker run --env-file env/production/django.env -d -p 8003:8002 django-app:1.0
```

## Running Nginx in production
```
docker build -t portfolio-nginx nginx/

docker run --name ngx -d -p 8004:80 portfolio-nginx
```

