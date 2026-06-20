def f():
    def g():
        print("inside function g ")
    g()
    print("inside function f ")
f()        