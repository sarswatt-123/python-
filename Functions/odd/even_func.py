def is_even(num):
    """
    This function is for to check the num is odd or even 
    input - any intger num
    output - odd/even

    """
    if type(num)==int:
        if num%2==0:
            return "even"
        else:
            return "odd"  
    else:
        return "pagal hai kya "    

for i in range(1,11):
    x=is_even(i)
    print(x)

def power(a=1,b=1):
    return a**b 
print(power(2))   

