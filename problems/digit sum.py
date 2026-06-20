num = int(input("Enter three digit number : "))

# num = 345 

a= num%10
num = num//10

b= num%10
num=num//10

c= num%10

print(a+b+c)

