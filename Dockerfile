# use python 3.11 image
FROM python:3.11

# copy source file to /app
COPY ./ /app

# set working directory to docker
WORKDIR /app

# install packages
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# expose port 8000 to be used to received requests
EXPOSE 8000

# run application
CMD ["gunicorn",  "--bind", "0.0.0.0:5000", "src.app:create_app()"]
