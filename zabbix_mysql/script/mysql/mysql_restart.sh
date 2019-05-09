#!/bin/bash

ps -ef |grep -q "\-\-port=$1";if [ $? -eq 0 ] ; then  awk '{ print $22 }' /proc/`ps -ef |grep "\-\-port=$1"|awk '{ print $2 }'`/stat; else  echo  0 ; fi
