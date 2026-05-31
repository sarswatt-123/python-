# Write a program to find the greatest of four numbers entered by the user.

a=int(input("Enter the number a: "))
b=int(input("Enter the number b: "))
c=int(input("Enter the number c: "))
d=int(input("Enter the number d: "))

if(a>b and a>c and a>d):
    print("a is largest ")
elif(b>a and b>c and b>d ):
    print("b is largest ") 
elif(c>a and c>b and c>d):
    print("c is largest ")   
elif (d>a and d>b and d>c):
    print("d is largest ")