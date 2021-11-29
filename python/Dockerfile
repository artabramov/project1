FROM ubuntu:latest

# vim
RUN apt-get update
RUN apt-get install -y vim

# apache 2
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata
RUN apt-get install -y apache2
RUN apt-get install -y systemctl

# python 3.7 & pip
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt update
RUN apt install -y python3.7
RUN rm /usr/bin/python3
RUN ln -s python3.7 /usr/bin/python3
RUN apt-get -y install python3-pip

#
RUN apt-get install libapache2-mod-wsgi-py3

WORKDIR /var/www/html
COPY ./src/ ./
RUN mv --force /var/www/html/000-default.conf /etc/apache2/sites-available/000-default.conf
RUN pip install --no-cache-dir -r /var/www/html/requirements.txt
RUN mkdir ./app
COPY ./app/ ./app/

EXPOSE 80
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
