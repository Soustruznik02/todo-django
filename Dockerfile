FROM python:3.9.13-alpine3.16
RUN apk add --no-cache sqlite 
WORKDIR /opt/app
COPY . .   
RUN pip install -r requirements.txt