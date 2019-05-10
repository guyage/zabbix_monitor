#!/bin/bash
echo -n '{"data":['
flag=""
redis_port="6379 6380"
#for port in `ps aux |grep [redis]-server|awk -F: '{print $NF}'`
for port in $redis_port
do
 echo -en "$flag{\"{#REDISPORT}\": \"$port\"}"
 flag=",\n"
done
echo -n ']}'
