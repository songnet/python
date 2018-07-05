import mysql.connector
import os,sys

conn = mysql.connector.connect(user='root',password='123.0',host='127.0.0.1',database='test')
# mysql.connector.errors.InternalError: Unread result found 解决办法 buffered = true
cursor = conn.cursor(buffered=True)

# 执行 select
#select_sql = "select * from mytable"
#cursor.execute(select_sql)

#获取 总行数
print(cursor.rowcount)

# 获取一行-----------返回元组类型 list
#first = cursor.fetchone()
#print(first)

# 获取多行 如果前面有 fetch 语句 就会从 上一个 fetch 语句 后开始读取
#many = cursor.fetchmany(5) # 从2 到 6 条
#print(many)

# 获取所有 数据 同上
#all = cursor.fetchall()
#print(all)

# 打印数据
#for item in all:
#    print(item)

#for (id,name,age) in all:
#    print("ID:{} Name:{} Age:{}".format(id,name,age)) # string.format()

# insert update delete
# 需要使用 事务 原子性，一致性，隔离性，持久性 以银行转账为例子
# 需要关闭 自动提交的设置
#conn.autocommit(False)

sql_insert = "insert into mytable(name,age) values ('songnet',30)"
sql_update = "update mytable set age = '40' where id = 4"
sql_delete = "delete from mytable where id = '2'"

try:
    cursor.execute(sql_insert)
    print(cursor.rowcount)
    cursor.execute(sql_update)
    print(cursor.rowcount)
    cursor.execute(sql_delete)
    print(cursor.rowcount)
# 全部正确执行 使用 conn.commit()
    conn.commit()
    
except Exception as e:
    print(e)
    conn.rollback()
# 失败使用 conn.rollback()


#声明 conn 和cursor 之后要先关闭 cursor 再关闭 conn
cursor.close()
conn.close()