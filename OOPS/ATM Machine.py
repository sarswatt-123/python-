class Atm:
    #Constructor
    def __init__(self):
        self.pin = ""
        self.balance=0
        self.menu()
        print("Execution done ")

    def menu (self):
        user_input=input("""
        Hii how can i help u ??
        1.press 1 to create pin 
        2. press 2 to change pin 
        3. press 3 to check balance 
        4. press 4 to withdraw 
        5. Anything else to exit  
       """)
        if user_input =="1":
            #create pin 
            self.create_pin()
        elif user_input=="2":
            #change pin 
            self.change_pin()
            
        elif user_input =="3":
            #check balance
            self.check_balance()
            
        elif user_input== "4":
            #withdraw
            self.withdraw()
            
        else :
            exit()

    def create_pin(self):
        user_pin=input("Enter ypur pin ")
        self.pin=user_pin

        user_balance = int(input("Enter your balance"))
        self.balance=user_balance

        print("Pin created succesfully")
        self.menu()


    def change_pin(self):
        old_pin = input('enter old pin')

        if old_pin == self.pin:
            # let him change the pin
            new_pin = input('enter new pin')
            self.pin = new_pin
            print('pin change successful')
            self.menu()
        else:
            print('nai karne de sakta re baba')
            self.menu()
    

    def check_balance(self):
        user_pin=input('Enter your pin ')
        if user_pin==self.pin:
            print("Your balance is :",self.balance)
            self.menu()
        else:
            print("Chal nikal yaha se") 
            self.menu()   


    def withdraw(self):
        user_pin=input("Enter your pin ")
        if user_pin==self.pin:
            #allow to withdraw
            amount=int(input("Enter your amount "))
            if amount<=self.balance:
                self.balance = self.balance - amount 
                print("Withdrawl succesfully")
                print("your current balance is :",self.balance)
            else:
                print('saale gareeb')    
            self.menu()
        else :
            print("saale chor ")
            self.menu()

# Object creation         
obj=Atm()
 
