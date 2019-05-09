# zabbix_mysql
zabbix监控mysql(自动发现，参照percona监控修改)

##使用方式
1. 安转所需软件(以centos系统为例)
yum install php php-mysql
python环境安转MySQLdb

2. 创建监控用户，以下两个文件需配置该用户
mysql_slave_discover.py
ss_get_mysql_stats.php

3. 添加zabbix监控项配置文件
将mysql_basic_discover.conf添加到zabbix配置项中，需修改实际脚本存放位置

4. 导入模版zabbix_mysql_templates.xml

5. 修改脚本中对应需要监控的端口，以下两个文件需修改
mysql_discover.sh
mysql_slave_discover.py

6. zabbix添加需监控服务器，添加模版，会自动发现监控项及触发器

