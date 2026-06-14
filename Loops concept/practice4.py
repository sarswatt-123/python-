# 6. Write a program to calculate the factorial of a given number using for loop.

n= int(input("Enter the number : "))
fact=1
for i in range(1,n+1):
    fact=fact*i
    
print(f"The factorial of {n} is : {fact}")


# 7. Write a program to find the 1/1! + 2/2! + 3/3!+ ----------------n 

n = int(input("Enter the number : "))
result =0
fact=1
for i in range(1,n+1):
    fact=fact*i
    result= result + i/fact
print(result)    

