
# 导入整个文件
import function
import transfermoney
function.fun_print('第一个function!')

# 只导入某个文件中的一个function from *** import
#from function import fun_plus
#print(fun_plus(20,3))

# 文件读写
#function.fun_openfile("foo1111.txt","r")

# 面向对象
# 1.实例化对象
emp1 = function.Employee("songnet",100)
emp2 = function.Employee("zhangwt",2000)
# 2.调用方法
emp1.displayEmp()
emp2.displayEmp()
emp2.showCount()
# 3.访问属性
print(function.Employee.count)
print(function.Employee.__doc__)
# 可以增加属性
emp1.age = 201111
print(emp1.age)
# 或者使用 setattr  hasattr getsttr delattr
setattr(emp2,'age',111111111)
print(emp2.age);

# 子类调用父类中的方法、及其属性
person = function.Person()
person.childMethod()
person.parentMethod()
print(person.parentAtttr)

# 调用转账方法

if __name__ == '__main__':
    source = 1
    target = 2
    money = 3000
    db = pymysql.connect("localhost", "root", "toor", "spider", charset="utf8")
    try_money = TransferMoney(db)
    try:
       try_money.transfer(source,target,money)
    except Exception as e:
        print(e)
    finally:
        db.close()

transfermoney.TransferMoney()
