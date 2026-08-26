class Atm: 
    #constructor 
    def __init__(self):
        self.pin= ''
        self.balance = 0
        self.menu()

    def menu(self):
        user_input=input("""
        1. Press 1 to Create PIN
        2. Press 2 to Change PIN
        3. Press 3 to Check Balance
        4. Press 4 to Withdraw
        5. Press 5 to Exist
        Input - """)
        
        if user_input == '1':
            self.create_pin()

        elif user_input == '2':
            self.change_pin()

        elif user_input == '3':
            self.check_balance()

        elif user_input =='4':
            self.withdraw()
        elif user_input =='5':
            exit()
        else:
            # INVALID 
            print("Invalid Input! Try Again")
            self.menu()
    
    def create_pin(self):
        user_pin=input("Set PIN ")
        self.pin=user_pin

        user_balance = int(input("Enter Your Balance: "))
        self.balance = user_balance
        print("~PIN Created Successfully~")

        self.menu()

    def change_pin(self):
        old_pin=input("Enter PIN ")
        if old_pin == self.pin:
            new_pin=input("Enter New PIN ")
            self.pin=new_pin
            print("PIN Changed Successfully!")
            self.menu()
        else:
            print("Wrong PIN! Try Again ")
            self.menu()
    
    def check_balance(self):
        user_pin=input("Enter Your PIN ")
        if user_pin ==  self.pin:
            print(f"Balance: {self.balance}")
            self.menu()
        else:
            print("Enter Correct PIN to Check Balance!")
            self.menu()

    def withdraw(self):
        user_pin = input("Enter Your PIN ")
        if user_pin == self.pin:
            amount=int(input("Withdrawal Amount  "))
            if amount<=self.balance:
                print("Withdrawal Successfull!")
                self.balance-=amount
                print(f"Current Existing Balance {self.balance}")

            else:
                print("LOW Balance! Can not Withdraw!")
        else:
            print("Wrong PIN! Try Again!")
        self.menu()
        


obj=Atm()
