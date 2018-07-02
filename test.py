#简单输出
print('hello world')

# 打开一个文件
'''
fo = open("foo.txt", "w")
fo.write( "www.runoob.com!\nVery good site!\n")
# 关闭打开的文件
fo.close()
'''
# 缩进
'''
if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
    # 没有严格缩进，在执行时会报错
    print ("False")
'''
import sys; x = 'runoob'; sys.stdout.write(x + '\n')

# 字符串截取
'''
str = 'Hello World!'
print (str)           # 输出完整字符串
print (str[0])        # 输出字符串中的第一个字符
print (str[2:5])     # 输出字符串中第三个至第五个之间的字符串
print (str[2:])      # 输出从第三个字符开始的字符串
print (str * 2)       # 输出字符串两次
print (str + "TEST")  # 输出连接的字符串
'''
# python List
'''
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
 
print (list)               # 输出完整列表
print (list[0])            # 输出列表的第一个元素
print (list[1:3])          # 输出第二个至第三个元素 
print (list[2:])           # 输出从第三个开始至列表末尾的所有元素
print (tinylist * 2)       # 输出列表两次
print (list + tinylist)    # 打印组合的列表
'''
# python 元组 tuple 
# ****** list 可以更新  tuple 和 tinytuple 不允许更新
'''
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
print (tuple)               # 输出完整元组
print (tuple[0])            # 输出元组的第一个元素
print (tuple[1:3])          # 输出第二个至第三个的元素 
print (tuple[2:])           # 输出从第三个开始至列表末尾的所有元素
print (tinytuple * 2)       # 输出元组两次
print (tuple + tinytuple)   # 打印组合的元组
'''
# 字典 dictionary dict tinydict
'''
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
 
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
 
print (dict['one'])          # 输出键为'one' 的值
print (dict[2])              # 输出键为 2 的值
print (tinydict)             # 输出完整的字典
print (tinydict.keys())      # 输出所有键
print (tinydict.values())    # 输出所有值
'''
# 数据类型转换

# 算数运算符 
'''
 加、减、乘、除、取模、等同于 C# ；
 ** 幂 10**20 10的20次方
 // 取整 9.0//2.0 = 4.0
'''
# 比较运算符
'''
==  != <> > < >= <=
'''
# 逻辑运算符
'''
and or not 或 与 非
'''
# 成员运算符 
'''
in 、not in
'''
#通过索引迭代循环 for item in items、range 开始-结束、len() 返回长度
'''
fruits = ['banana','apple','mango'];
for index in range(len(fruits)):
    print('current fruit:',fruits[index]);
'''