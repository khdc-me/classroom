#Dockerize WordPress
Set up a WordPress instance inside of a docker container.

##Goal
Practice installing a standalone app inside of a docker container.

Will use Nginx and MySQL docker containers but will download the latest version of WordPress onto the host and build my container, copying the local WP package into the container simultaneously.

##Steps
From host, download [latest WordPress](https://wordpress.org/latest.tar.gz) (at the time of this writing v5.2.2)

Created "wordpress" folder

Extracted WP tar.gz files into "wordpress" folder

Created "mysql" folder

Added Dockerfile inside of "mysql" folder to build a mysql container (latest version at time of writing is 8.0.17)
> [Official mysql docker image](https://hub.docker.com/_/mysql/)

Created "apache" folder

Added Dockerfile inside of "apache" folder to build a php+apache container (latest non-rc/beta version at time of writing is 7.1.31-apache-stretch)