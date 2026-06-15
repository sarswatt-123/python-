def is_even(num):
    if num%2==0:
        return ("even")
    else:
        return("odd")
print(is_even(7))        
for i in range(1,11):
    x=is_even(i)
    print(x)
    
def power(a=1,b=1):
    return a**b 
print(power(2))   

# How to acces and print the docstring of any function 

print(is_even.__doc__)


print(print.__doc__)
print(type.__doc__)