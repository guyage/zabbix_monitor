#!/bin/bash
echo -n '{"data":['
flag=""
mysql_port="3306 3307"
for port in $mysql_port
do
 echo -en "$flag{\"{#MYSQLPORT}\": \"$port\"}"
 flag=",\n"
done
echo -n ']}'
