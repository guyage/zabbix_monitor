#!/usr/bin/python 
#coding:utf-8 
 
import MySQLdb 
import sys 
 
class check_mysql_repl(): 
    def __init__(self): 
        self.dbhost = '127.0.0.1' 
        self.dbuser = 'zabbix' 
        self.dbpass = 'zabbix' 
        self.dbport = int(sys.argv[1])
        #self.sock = "/xs/data/mysql/37891/mysql37891.sock" 
 
        self.conn = MySQLdb.connect(host=self.dbhost,port=self.dbport,user=self.dbuser,passwd=self.dbpass) 
        self.cursor = self.conn.cursor(cursorclass = MySQLdb.cursors.DictCursor) 
        self.execsql = 'show slave status' 
        self.cursor.execute(self.execsql) 
        self.data = self.cursor.fetchall() 
        self.io = self.data[0]['Slave_IO_Running'] 
        self.sql = self.data[0]['Slave_SQL_Running'] 
        self.slavelag = self.data[0]['Seconds_Behind_Master']
        self.conn.close() 
 
    def get_io_status(self): 
        if self.io == 'Yes': 
            return 1 
        else: 
            return 0 
 
    def get_sql_status(self): 
        if self.sql == 'Yes': 
            return 1 
        else: 
            return 0                
     
    def get_slavelag(self):
        return self.slavelag
 
 
if __name__ == "__main__": 
    if len(sys.argv) != 3: 
        print "Usage: %s [port slave_running|port slavelag]" % sys.argv[0] 
        sys.exit(1) 
    mysql = check_mysql_repl() 
    if sys.argv[2] == "slave_running":
        io_status = mysql.get_io_status()
        sql_status = mysql.get_sql_status()
        print io_status + sql_status
    #if sys.argv[2] == "io": 
    #    print mysql.get_io_status() 
    #elif sys.argv[2] == "sql": 
    #    print mysql.get_sql_status()
    elif sys.argv[2] == "slavelag":
        print mysql.get_slavelag()
