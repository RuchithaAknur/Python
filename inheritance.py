class Bank:
    Bank_name="BOB"
    def __init__(self,name,balance,acc_no):
        self.name=name
        self.balance=balance
        self.acc_no=acc_no
    def show(self):
        print(f"available person:{self.name} and balance:{self.balance}")
class ATM(Bank):
    def __init__(self,name,balance,acc_no,atm_loc,pin):
        super().__init__(name,balance,acc_no)
        self.atm_loc=atm_loc
        self.pin=pin
    def display(self):
        print(f"The ATM is at {self.atm_loc}")
    def withdraw(self,amount):
        if amount>self.balance:
            print("insuffient balance")
        else:
            self.balance-=amount
            print(f"amount:{amount} debited sucessfully")
        
a1=ATM("ruchitha",50000,897836763,"hyd",6293)
a1.display()
a1.show()
a1.withdraw(2000)
