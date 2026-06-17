# concept of *args and *kwargs 

def multiply(*args):
    product=1
    print(args)
    for i in args:
        product = product * i 
    return product

print(multiply(4,6,7,8,6,7,4,2,3))

# concept of **kwargs 

def display(**kwargs):
    for (key,value) in kwargs.items():
        print(key,"->",value)
print(display(india="delhi",nepal="kathmandu",pakistan="islamabad"))