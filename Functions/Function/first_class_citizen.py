def square(n):
    return n*n
print(square(4))
print(type(square))

x=square
print(id(x))



L=[2,4,56,square]
print(L)

def f():
    def x(a, b):
        return a+b
    return x
    
val = f()(3,4)
print(val)




def func_a():
    print('inside func_a')

def func_b(z):
    print('inside func_c')
    return z()

print(func_b(func_a))