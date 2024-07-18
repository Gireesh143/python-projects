class swiss :
    ROI = 0.5
    Branch_Name = "marthahalli"
    def __init__(self,name,accno,mbno,bal,password):
        self.name = name
        self.accno = accno
        self.mbno = mbno
        self.bal = bal
        self.password = password
    def details(self):
        print(f'Name : {self.name}')
        print(f'Accno : {self.accno}')
        print(f'Mbno : {self.mbno}')
        print(f'Balance : {self.bal}')
    @staticmethod
    def enterpin():
        p = int(input('Enter the pin: '))
        return p
    def checkingbal(self):
        if self.enterpin()==self.password:
            print(f'Available Balance is : {self.bal}')
        else:
            print("Entered wrong pin")
    def deposit(self,money):
        if self.password==self.enterpin():
            print("Amount deposited successfully.")
            self.bal+=money
            print(f'Available balance {self.bal}')
        else:
            print("Entered wrong pin")
    def withdraw(self,money):
        if self.enterpin()==self.password:
            if self.bal>=money:
                print("Amount withdrawn successfully.")
                self.bal-=money
                print(f'Available balance {self.bal}')
            else:
                print("Insufficient balance.")
        else:
            print("Entered wrong pin")


user1 = swiss('Gireesh',2738193009,6281096138,1000000,6281)
user2 = swiss('sai',42817875872,742387582,200000,1432)
user1.deposit(2000)
user1.deposit(1000)









