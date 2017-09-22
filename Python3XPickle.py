# Python3X中只有pickle模块。移除了cPickle模块
# Pickle模块会对封装对象的属性名称进行管制，如封装了许多同名对象，那么这些对象必须具有相同的属性名称。
# 不必给每个对象多次存在相同的字符串(属性名称)，只需保存一个包含所有属性名称的一个表，并保存每个属性的索引即可
# 或者 仅保存向每个对象的标准属性名称集合中增加或删除的动态属性
# 这样做能够做到尽量减小封装，所以能够更快的加载或拆封

# 移除了imageop,audiodev,Bastion,bsddb185,exceptions,linuxaudiodev,md5,MimeWriter,mimify,popen2,rexec,sets,sha,stringold
# strop,sunaudiodev,timing,xmlib,bsddb,new模块

if __name__ == "__main__":
    import pickle

    obj = 123, "abcdef", ["abc", 123], {"key": "value", "key1": "value1"}
    print("obj_pickle:", obj)

    file_name = "tmp/obj_pickle_dump.txt"
    f = open(file_name, "wb")
    pickle_dump = pickle.dump(obj, f)  # dump到文件中
    print(type(pickle_dump))  # <class 'NoneType'>
    print("pickle_dump:", pickle_dump)
    f.close()

    f = open(file_name, "rb")
    print("pickle.load:", pickle.load(f))

    obj_pickle_dump = pickle.dumps(obj)  # dump到内存中
    print(type(obj_pickle_dump))
    print("obj_pickle_dump:", obj_pickle_dump)

    obj_pickle_load = pickle.loads(obj_pickle_dump)
    print("obj_pickle_load:", obj_pickle_load)


# nonlocal声明。使用nonlocal可以声明一个外部变量(不是global变量)
def out_function():  # 外层函数
    call_count = 0

    def in_function():  # 内层函数
        nonlocal  call_count  # 调用外层函数的属性。注掉此行，会报错UnboundLocalError: local variable 'call_count' referenced before assignment
        call_count += 1
        call_count += 1
        print("call_count:", call_count)  # call_count: 2

    return in_function


out_function()()
