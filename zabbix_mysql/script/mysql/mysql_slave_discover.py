#!/usr/bin/python 
#coding:utf-8 
 
import MySQLdb 
import sys
import json

db_host = '127.0.0.1'
db_user = 'zabbix'
db_passwd = 'zabbix'
db_port = ['3306','3307']
slave_port = []
role = 'slave'

for port in db_port:
    conn = MySQLdb.connect(host=db_host,user=db_user,passwd=db_passwd,port=int(port))
    cur = conn.cursor()
    cur.execute("show slave status;")
    results = cur.rowcount
    cur.close()
    conn.close()
    
    if results == 1:
        slave_port.append({'{#MYSQLPORT}':port,'{#MYSQLROLE}':role})
        
print json.dumps({'data':slave_port},indent=4,separators=(',',':'))
