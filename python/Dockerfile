FROM python:3.7
RUN apt-get update
RUN mkdir /app
WORKDIR /app

# vim
RUN apt-get install -y vim
RUN git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim
RUN git clone https://github.com/artabramov/vim.git ~/.tmp
RUN cp /root/.tmp/.vimrc /root/
RUN rm -R /root/.tmp

# apache
RUN apt-get install -y apache2 apache2-dev
RUN a2enmod rewrite
RUN apt-get clean

# venv
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

# app
COPY ./app/ ./

EXPOSE 80
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
