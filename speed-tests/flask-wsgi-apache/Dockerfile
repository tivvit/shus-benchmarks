############################################################
# Dockerfile to build Flask App
# Based on
############################################################

# Set the base image
FROM python-flask as flask

FROM debian:latest

RUN apt-get update && apt-get install -y apache2 \
    libapache2-mod-wsgi-py3 \
    build-essential \
    python \
    python3-dev\
    python3-pip

RUN pip install flask==1.1.1 PyYAML==5.3

# Copy over the apache configuration file and enable the site
COPY flask-wsgi-apache/apache-flask.conf /etc/apache2/sites-available/apache-flask.conf
RUN a2ensite apache-flask
RUN a2enmod headers
RUN a2enmod wsgi

# Copy over the wsgi file
COPY flask-wsgi-apache/apache-flask.wsgi /var/www/apache-flask/apache-flask.wsgi

COPY --from=flask /app /var/www/apache-flask/

RUN a2dissite 000-default.conf
RUN a2ensite apache-flask.conf

EXPOSE 80

WORKDIR /var/www/apache-flask

# CMD ["/bin/bash"]
CMD  /usr/sbin/apache2ctl -D FOREGROUND
# The commands below get apache running but there are issues accessing it online
# The port is only available if you go to another port first
# ENTRYPOINT ["/sbin/init"]
# CMD ["/usr/sbin/apache2ctl"]