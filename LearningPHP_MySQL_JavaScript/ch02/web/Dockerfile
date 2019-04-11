FROM php:7.3.4-apache-stretch

ENV MYSQL_USER=mysql_admin \
	MYSQL_PASSWORD=mysql_password \
	MYSQL_ROOT_PASSWORD=mysql_root_password

RUN docker-php-ext-install mysqli
RUN docker-php-ext-enable mysqli