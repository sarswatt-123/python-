#  3. User will input (2numbers).Write a program to swap the numbers

# without using temporary variable 
num1 = int(input("Enter the number 1 :"))
num2 = int(input("Enter the number 2 "))

"""(num1,num2) = (num2,num1)

print("number 1 ",num1)
print("number",num2)"""

#without using temporary variable 
t=num1
num1=num2
num2=t
print("num 1 :",num1)
print("num2:",num2)


