# 1. User will input (3 ages).Find the oldest one

a1=int(input("Enter your age "))
a2=int(input("Enter your age "))
a3=int(input("Enter your age "))

if(a1>a2 and a1>a3 ):
    print("a1 age is older :",a1)
if(a2>a1 and a2>a3 ):
    print("a2 age is older :",a2)
if(a3>a2 and a3>a1 ):
    print("a3 age is older :",a3)