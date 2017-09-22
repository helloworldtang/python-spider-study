# Python3.x新特性
# http://www.maiziedu.com/course/673-9999/
import platform
import timeit
import io

# print在Python3.X中是一个函数，不再是一个语句
# 打开文件fid.txt为写入作准备，并将对象指定给fid,再使得print将一个字符串重定向给文件fid
fid = open("tmp/fid.txt", "w")
print("test print to file", file=fid)
print("hello")

# 连接符
print("one", "two", sep="_")


# exec()作为函数，只操作globals()和locals()函数返回的字典。
# locals()函数返回的字典实际上是局部变量的一个副本
# exec()函数中进行的赋值只修改了局部变量的这份副本，而非局部变量本身
def foo():
    _locals = locals()
    exec('a=4', globals(), _locals)
    a = _locals['a']
    print(a)


foo()

# 4

# 进制转换
number = 666
oct_666 = oct(number)
print("oct_666", oct_666, sep=":")
bin_666 = bin(number)
print("bin_666", bin_666, sep=":")

# input()会从标准输入(sys.stdin)读取一个输入并返回一个字符串，且尾部的换行符从末尾移除
# input_str = input("请输入一个字符串:")
# print(input_str)
#
# input_express = eval(input("请输入一个有效的Python表达式(譬如1+2):"))
# print(input_express)

# for 在Python3.X中，for循环中的变量不再会泄漏到全局命名空间中了
# print('Python', copyright())

print("Python", platform.python_version())
i = 1
print('before:i', i)
print('comprehension:', [i for i in range(5)])
print('after:i=', i)

# range
# 在Python3.X中，range()的实现方式与xrange()相同，xrange()改名为range()。
# 在Python3中使用xrange()会触发NameError。
# 同时range()会返回可迭代对象而不再是列表，
# 要想使用range()获取一个list，必须显示调用list(range(10))
print("range to list ", list(range(10)), sep=":")


def test_range():
    for i in range(100):
        pass


if __name__ == '__main__':
    print("Python version", platform.python_version(), sep=":")
    # timeit.Timer
    # 测试一行代码的运行时间,在python中比较方便,可以直接使用timeit
    during = timeit.Timer("test_range()", "from __main__ import test_range")
    print("test_range", during.timeit())

# dict
# dict.iterkeys()、dict.itervalues()和dict.iteritems()方法被.keys()、.values()和.items()取代
# 它们返回类似于集的可迭代对象，而不是key和value的列表。
# 从而在不进行key和value复制的情况下，就能在其上执行set操作
print("==============dict==============")
dict_tmp = {1: "hello", 2: "world"}
print(dict_tmp.items())
for values in dict_tmp.items():
    print(values)
keys = list(dict_tmp.keys())
print(keys)
values = list(dict_tmp.values())
print(values)

# Python3.X具有单一的字符串类型str，其功能类似于版本2.X的unicode类型。
# Python3.X中所有字符串都是unicode字符串。这种改变使得Python3.X对非拉丁文的文本，非ASCII标识也是允许的
print(repr('λ'))  # 返回unicode字符串。在python2.X中repr会将此latin字符转换成ASCII
α_pronounce = "a er fa"
print("α_pronounce", α_pronounce, sep=":")

# Python3.X新增了bytes类型，对应于2.X版本的八位串
# 定义一个bytes类型的变量的方法如下：
b = b'china'
print("字符串b的数据类型", type(b), sep=":")

# str对象到bytes对象的转换：可以使用.encode() 完成str->bytes
# bytes对象和str对象的转换：可以使用decode()完成 bytes->str
s_var = b.decode()  # bytes类型转换成str类型
print("bytes类型转换成str对象", s_var, sep=":")
byte_var = s_var.encode()  # str类型转换成byte类型
print("str对象转换成bytes类型", byte_var, sep=":")

# IO
# Python3.X的IO系统反映了文本和字符串形式的二进制数据之间的巨大差异
# 1、 如果要对文本执行任何I/O操作，Pytho3.X会强制要求显式使用“文本模式”打开文件
# 1、 如果要对二进制数据执行I/O操作，必须使用“二进制模式”打开文件，并且使用字节字符串
# 提供自定义编码的能力，如果不想使用默认编码（通常为UTF-8），还需提供可选的编码方式
# 常见的错误是将输出数据传递给错误模式打开的文件或I/O流

f = open("tmp/foo_wb.txt", "wb")  # 以二进制写模式打开
# f.write("Hello world\n") #因为写入的是str对象，但预期是bin，所以foo.txt文件没有内容写入
for i in range(5):
    f.write(b"Hello world\n")

f = open("tmp/foo_w_encoding.txt", "w", encoding='ASCII')
# f.write("中文")  # UnicodeEncodeError: 'ascii' codec can't encode characters in position 14-15: ordinal not in range(128)
f.write("Hello world foo_w_encoding")

file_name = "tmp/foo_w.txt"
f = open(file_name, "w")  # 以写方式打开
for i in range(5):
    f.write("Hello world\n")
f.close()

# 打开一个输入/输出流除了使用内置的open(fileName)函数以外，也可以调用io.open(fileName)返回文件句柄
# read()和readline()函数用于文件内容的读取（Python3.X内的所有字符串都是unicode)

# io.open也可以打开
print("===============io.open===============")
f = io.open(file_name, "rb")
print("io.open", f, sep=":")  # 是一个句柄<_io.BufferedReader name='tmp/foo_w.txt'>
f.close()

print("===============f.readline()===============")
f = open(file_name, "rb")
line = f.readline()  # 只返回一行
print("readline()", line, ":")
f.close()

print("===============open===============")
for line in open(file_name, "rb"):
    print(line)

fo = open(file_name, "r")
print("name of the file:", fo.name)

print("===============f.readlines()===============")
f = open(file_name, "r")
for line in f.readlines():
    print(line)  # 读取全部，返回一个可迭代对象
f.close()

print("===============f.read()===============")
f = open(file_name, "rb")
print(f.read())  # 全部读取，但会把换行符去掉
f.close()

# 返回可迭代对象
# Python3.X中某些函数和方法在Python3.X中返回的是可迭代对象，而不是在Python2.X中返回列表
print("Python", platform.python_version())
print(range(3))
print(type(range(3)))  # <class 'range'>,Python2.X中返回的是<type 'list'>
# 通常迭代对象只遍历一次，所以这种方式会节省内存
# 然而如果通过生成器多次迭代这些对象，效率就不高
# 如果需要列表对象，可以通过list()函数简单的将可迭代对象转换成列表
print(list(range(3)))  # list()将迭代对象转换成列表
for i in range(3):
    print("value:", i, sep=":")

# Python3.X中其它不再返回列表的常用函数和方法：
# zip()/map()/filter()/字典的.key()/字典的.value()/字典的.item()方法
# 其它的函数apply(),callable(),coerce(),execfile(),reduce(),reload()都被去除了


# raise Exception
# Python3只接受带括号的语法，否则语法错误SyntaxError
# print("Python", platform.python_version())
# raise IOError("file error")

# 异常处理中next的使用
# Python3.X中，只能使用next()函数，调用对象的.next()行为会触发AttributeError，因为已经对象已经没有.next()行为了

print("Python", platform.python_version())
my_generator = (letter for letter in 'abcdefg')
print(my_generator)
next(my_generator)
print(my_generator)

try:
    let_us_cause_a_NameError
except NameError as err:
    print(err, '-->test as syntax')
