
from time import ctime,sleep


def music():
    for i in range(2):
        print( "I was listening to music. %s" %ctime())
        sleep(1)

def move():
    for i in range(2):
        print("I was at the movies! %s" %ctime())
        sleep(5)

if __name__ == '__main__':
    music()
    move()
    print("all over %s" %ctime())



import threading
from time import ctime,sleep
def music(func):
    for i in range(2):
        print("i was listening to %s.%s" %(func,ctime()))
        sleep(1)

def move(func):
    for i in range(2):
        print("i was at the %s! %s" %(func,ctime()))
        sleep(5)

def book(func):
    for i in range(2):
        print("i was look the %s.%s" %(func,ctime()))
        sleep(4)

threads=[]
t1=threading.Thread(target=music,args=(u"爱情买卖",))
threads.append(t1)
t2=threading.Thread(target=move,args=(u"阿凡达",))
threads.append(t2)
t3=threading.Thread(target=book,args=(u"python",))
threads.append(t3)


if __name__=='__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

    print("all over %s" %ctime())




import _thread as thread,time

def counter(myid,count):
    for i in range(count):
        time.sleep(1)
        print("[%s]=>%s" %(myid,i))


for i in range(5):
    thread.start_new_thread(counter,(i,5))
    time.sleep(6)
    print("Main thread exiting.")
