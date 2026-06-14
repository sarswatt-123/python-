import random
jackpot=random.randint(1,100)
guess=int(input("Enter the number "))
counter=1
while(jackpot!=guess):
    if(guess < jackpot):
        print("You have too low ")
    else:
        print("you have too high ")    
        
    guess=int(input("Enter the number "))
    counter+=1

else:
    print("Shi guess kiya ")   
print("you have take attempts :",counter)
