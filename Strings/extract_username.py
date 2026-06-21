# How to extract username from email 

email= input("Enter your mail id : ")
pos=email.index("@")
print(email[0:pos])