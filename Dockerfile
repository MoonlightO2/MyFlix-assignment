FROM ubuntu:14.04
MAINTAINER Shashini Peiris "shashpeiris@gmail.com"
ENV REFRESHED_AT 2023-01-10
RUN apt-get update
RUN apt-get install -y nginx
RUN mkdir -p /var/www/html
ADD nginx/global.conf /etc/nginx/conf.d/
ADD nginx/nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
ENTRYPOINT ["/usr/sbin/nginx"]
