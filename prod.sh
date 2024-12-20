docker build -t sales-import-generator .
# docker run --name relieph-dev -d -p 8000:80 sales-import-generator
docker run --name sales-import-generator-app -d -p 8000:8000 sales-import-generator
docker container logs sales-import-generator-app
