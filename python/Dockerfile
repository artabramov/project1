FROM python:3.7

# apache
RUN apt-get -y update
RUN apt-get install -y apache2 apache2-dev
#RUN apt-get install -y libapache2-mod-wsgi-py3
RUN apt-get clean

# venv
RUN mkdir /app
WORKDIR /app
RUN python3.7 -m venv ./virtualenv
RUN ./virtualenv/bin/pip3.7 install mod_wsgi
RUN ln -s /app/virtualenv/lib/python3.7/site-packages/mod_wsgi/server/mod_wsgi-*.so /app/virtualenv/lib/python3.7/site-packages/mod_wsgi/server/mod_wsgi.so

# requirements
COPY ./src/requirements.txt ./
RUN ./virtualenv/bin/pip3.7 install --no-cache-dir -r ./requirements.txt
RUN rm ./requirements.txt

# apache conf
COPY ./src/000-default.conf ./
RUN mv --force ./000-default.conf /etc/apache2/sites-available/000-default.conf

COPY ./app/ ./

#WORKDIR /var/www/html
#COPY ./src/ ./
#RUN mv --force /var/www/html/000-default.conf /etc/apache2/sites-available/000-default.conf
#RUN pip3.7 install --no-cache-dir -r /var/www/html/requirements.txt
#RUN mkdir app
#COPY ./app/ ./app/

EXPOSE 80
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]