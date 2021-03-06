'''
python 3.6 连接mysql https://www.cnblogs.com/kungfupanda/p/5774917.html
1.本机安装 mysql
2.安装python-3.6.0.exe
3.安装 mysql-connector-python-8.0.11-py3.6-windows-x86-64bit.msi https://dev.mysql.com/downloads/connector/python/
4.下载VC++ 6.0
5.pip install mysql-python

****** Microsoft Visual C++ 14.0 is required  https://blog.csdn.net/TH_NUM/article/details/77095177

'''
import mysql.connector;
import sys,os;

user = 'root'
#pwd  = '123.0' 笔记本
pwd  = 'wocao123.0' # 公司笔记本
host = '127.0.0.1'
db   = 'test'

data_file = 'mysql-test.dat'
 
create_table_sql = "CREATE TABLE IF NOT EXISTS mytable ( \
                    id int(10) AUTO_INCREMENT PRIMARY KEY, \
    name varchar(20), age int(4) ) \
    CHARACTER SET utf8"
 
insert_sql = "INSERT INTO mytable(name, age) VALUES ('Jay', 22 ), ('杰', 26)"
select_sql = "SELECT id, name, age FROM mytable"
 
 # 创建 mysql连接对象
cnx = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
# 创建游标对象
cursor = cnx.cursor()
 
try:
    cursor.execute(create_table_sql) # 执行sql语句
except mysql.connector.Error as err:
    print("create table 'mytable' failed.")
    print("Error: {}".format(err.msg))
    sys.exit()
 
try:
    cursor.execute(insert_sql) # 执行sql语句
except mysql.connector.Error as err:
    print("insert table 'mytable' failed.")
    print("Error: {}".format(err.msg))
    sys.exit()
 
if os.path.exists(data_file):
    myfile = open(data_file)
    lines = myfile.readlines()
    myfile.close()
 
    for line in lines:
        myset = line.split()
        sql = "INSERT INTO mytable (name, age) VALUES ('{}', {})".format(myset[0], myset[1])
        try:
            cursor.execute(sql)
        except mysql.connector.Error as err:
            print("insert table 'mytable' from file 'mysql-test.dat' -- failed.")
            print("Error: {}".format(err.msg))
            sys.exit()
 
try:
    cursor.execute(select_sql)
    for (id, name, age) in cursor:
        print("ID:{}  Name:{}  Age:{}".format(id, name, age))
except mysql.connector.Error as err:
    print("query table 'mytable' failed.")
    print("Error: {}".format(err.msg))
    sys.exit()
 
cnx.commit()
cursor.close()
cnx.close()

