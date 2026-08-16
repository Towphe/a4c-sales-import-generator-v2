docker build -t sales-import-generator .
# docker run --name relieph-dev -d -p 8000:80 sales-import-generator
docker run --name sales-import-generator-app -d -t -p 5000:5000 sales-import-generator
docker container logs sales-import-generator-app
