FROM debian:latest


RUN apt-get update && apt-get install -y apache2 \
    libapache2-mod-wsgi-py3 \
    build-essential \
    python3 \
    python3-pip \
    python3-git \
    python3-dev\
    vim \
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*


RUN apt-get update -y
RUN apt-get install -y gir1.2-gobject-2.0 
RUN apt-get update -y
RUN apt-get install -y libpango-1.0-0
RUN apt-get install -y libpangoft2-1.0-0

COPY ./requirements.txt /var/www/apache-flask/app/requirements.txt

RUN pip install -r /var/www/apache-flask/app/requirements.txt
COPY ./apache-flask.conf /etc/apache2/sites-available/apache-flask.conf
RUN a2ensite apache-flask
RUN a2enmod headers

COPY ./apache-flask.wsgi /var/www/apache-flask/apache-flask.wsgi
COPY ./run.py /var/www/apache-flask/run.py
COPY ./app /var/www/apache-flask/app/

RUN a2dissite 000-default.conf
RUN a2ensite apache-flask.conf
RUN ln -sf /proc/self/fd/1 /var/log/apache2/access.log && \
    ln -sf /proc/self/fd/1 /var/log/apache2/error.log


RUN chown -R www-data:www-data /var/www/apache-flask/app/static
RUN chmod 755 /var/www/apache-flask/app/static
VOLUME /var/www/apache-flask
EXPOSE 80
WORKDIR /var/www/apache-flask
CMD  /usr/sbin/apache2ctl -D FOREGROUND
