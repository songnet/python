
import os

# 基本 function 定义
def fun_print(temp):
    print("hello : ",temp)
    return

def fun_plus(temp1,temp2):
    return temp1 + temp2

# filename accessmode buffering
def fun_openfile(filenname,mode):
    #打开文件
    file = open(filenname,mode)
    print(file.name)
    print(file.closed)
    print(file.readline())
    file.close()

# 面向对象
class Employee: # 类名
    '员工基类' # 内置 __doc__
    count = 0 # 外部属性
    parentAtttr = "父类中的变量"
    def __init__(self,name,salary): #构造函数、初始化
        print("父类中的构造函数")
        self.name = name
        self.salary = salary
        Employee.count += 1

    def showCount(self):
        print("employee的数量是：",Employee.count)

    def displayEmp(self):
        print("name:",self.name,"salary:",self.salary)

    def parentMethod(self):
        print("调用父类中的方法")

# 类的继承
class Person (Employee):
    'Person类，继承Employee'

    def __init__(self):
        print("子类中的构造函数")

    def childMethod(self):
        print("调用子类中的方法")