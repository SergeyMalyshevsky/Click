# set base image (host OS)
FROM python:3.8-alpine3.14

# copy the content of the local src directory to the working directory
COPY . /code/

# set the working directory in the container
WORKDIR /code

# install packages
RUN apk add jpeg-dev zlib-dev
RUN apk add --virtual .build-deps build-base linux-headers

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# create sqlite database
RUN python manage.py makemigrations
RUN python manage.py migrate

# command to run on container start
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
