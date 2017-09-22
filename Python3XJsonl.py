# Python3.X中，json模块获取了一个C扩展，这使得性能有了显著提高
# http://www.maiziedu.com/course/673-10006/

# 以下程序创建一个嵌套数据结构，该结构由一个字典列表构成，
# 而字典又包含其它存放基本值的字典的列表。
# 下例将整个列表串行化为一个JSON，然后又返回
from __future__ import with_statement
import sys
import time
import json


def test_json():
    data_dict = dict(a=1, b='BBBB', c=4.56)
    data_dict_6times = 6 * [data_dict]
    print("data_dict_6times:", data_dict_6times)
    nest_dict = dict(z=data_dict_6times, zz=2 * data_dict_6times, zzz=3 * data_dict_6times)
    print("============dict json============")
    print(nest_dict)
    nest_dict_100times = 100 * [nest_dict]
    start = time.time()
    dict_json_dump = json.dumps(nest_dict_100times)
    assert json.loads(dict_json_dump) == nest_dict_100times
    end = time.time() - start
    return end


test = test_json

if __name__ == '__main__':
    times = [test() for i in range(10)]
    times.remove(max(times))
    times.remove(min(times))
    print("Average:", sum(times) / len(times))
