s=set()
s.add(8)
s.add("8")
print(s)

t=set()
t.add(20)
t.add(20.0)     # python 20 and 20.0 ko same treat krta hai kyuki wo numercially compare krega dono ko ki same value hai ki nhi 
t.add("35")
print(len(t))
