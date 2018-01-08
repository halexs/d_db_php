FROM mysql/mysql-server:5.6
COPY setup.sql /docker-entrypoint-initdb.d/setup.sql

# FROM mysql:5.6
#COPY setup.sh /mysql/setup.sh
#COPY setup.sql /mysql/setup.sql
#RUN chmod 755 /mysql/setup.sh
#RUN /mysql/setup.sh