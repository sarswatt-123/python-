"""
3. A spam comment is defined as a text containing following keywords: “Make a lot of
money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

"""
# ---------------------------Solution ------------------------------------------


p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"

mssg= input("Enter your comment here : ")
if(p1 in mssg or p2 in mssg or p3 in mssg or p4 in mssg):
    print("your comment is a spam")
else:
    print("Your comment is not a spam")