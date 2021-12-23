FROM httpd:alpine
RUN mkdir /logs

# Install System Dependencies
# =============================================================================
RUN apk --update --no-cache add chromium-chromedriver apache2-mod-wsgi libffi-dev \
	wget ca-certificates make gcc musl-dev
COPY requirements.txt /var/www/app/requirements.txt

# Install Python and Python Dependencies
# =============================================================================
RUN apk --update --no-cache add python3-dev && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install -r /var/www/app/requirements.txt
RUN pip3 install pika

# Handle Apache2 Configuration, Remove Excess Files
# =============================================================================
COPY httpd.conf /var/www/app/httpd.conf
RUN cat /var/www/app/httpd.conf > /usr/local/apache2/conf/httpd.conf
RUN rm /var/www/app/requirements.txt /var/www/app/httpd.conf

# Start Apache2 Server
# =============================================================================
COPY . /var/www/app
EXPOSE 80 443
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND", "-f", "/usr/local/apache2/conf/httpd.conf"]
