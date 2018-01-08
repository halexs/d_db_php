#!/bin/bash
set -e
#service mysql start
mysql -uroot -proot < /mysql/setup.sql
#service mysql stop