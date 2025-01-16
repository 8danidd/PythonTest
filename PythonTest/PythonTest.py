from time import sleep

def fun1():
    a = 2
    global b
    while (a / 5 != 200):
        print("current number:", a)
        sleep(.001)
        b = a = (a + 1)
    print("final number:", a)

def fun2():
    global b
    while (b > 50):
        print("current number:", b)
        sleep(.001)
        b = b - 1
    print("final number:", b)

fun1()
sleep(3)
fun2()