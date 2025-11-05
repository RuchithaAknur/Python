def fun1(num):
    x=200
    print("outer function")
    print(num)
    def fun2():
        print("inner function")
        print(num)
        print(x)
    fun2()
x=100
fun1(100)
