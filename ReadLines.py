from __future__ import with_statement
import sys
import time

print("version_info:", sys.version_info[0])
if sys.version_info[0] == 3:
    exec("c=b'X'")
else:
    c = 'X'


def test_write_speed():
    start = time.time()
    with open("1.txt", "wb") as f:
        for i in range(50000):
            f.write(c)
    end = time.time() - start
    print(end)
    return end


times = [test_write_speed() for i in range(10)]
times.remove(max(times))
times.remove(min(times))
print("Average", sum(times) / len(times))
