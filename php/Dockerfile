FROM ubuntu:latest

# vim
RUN apt-get update
RUN apt-get install -y vim

# apache 2
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata
RUN apt-get install -y apache2
RUN apt-get install -y systemctl

# php 7.0
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:ondrej/php
RUN apt-get update
RUN apt install -y php7.0 libapache2-mod-php7.0 php7.0-cli php7.0-common php7.0-xml php7.0-zip
RUN echo "<?php phpinfo();" >> /var/www/html/index.php

# composer & codeigniter 3
RUN apt update
RUN apt install curl
RUN curl -sS https://getcomposer.org/installer -o /var/www/html/composer-setup.php
RUN php /var/www/html/composer-setup.php --install-dir=/var/www/html
RUN php -r "unlink('/var/www/html/composer-setup.php');"
RUN php /var/www/html/composer.phar create-project kenjis/codeigniter-composer-installer /var/www/html/codeigniter

WORKDIR /var/www/html
COPY ./src/ ./
RUN mv --force /var/www/html/000-default.conf /etc/apache2/sites-available/000-default.conf

EXPOSE 80
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
