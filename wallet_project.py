#wallet tracker
class wallet :
    def __init__(self, initial_balance=0,check=None):
        self.balance = initial_balance
        self.pin = check
    def addingaccount(self,account,pin):
        self.account = account
        self.pin = pin
        #self.account = int(input("enter the 12 digit account number : "))
        #self.pin = input("enter the unique pin of 9 characters :")
        l_c = 0
        u_c = 0
        d_c = 0
        s_c = 0
        for i in self.pin :
            if len(self.pin) > 8:
                if i.islower() :
                    l_c += 1
                elif i.isupper() :
                    u_c += 1
                elif i.isdigit() :
                    d_c += 1
                elif i in "!@#$%^&*()_+" :
                    s_c += 1
        if u_c >= 1 and l_c >= 1 and d_c >= 1 and s_c >= 1 :
            print("the pin which you have entered is valid and strong !")
            print("your account has been created succesfully and your account number is :",self.account)
    def addamount(self,amount,checkpin = None):
        #check = input("enter the pin to add amount : ")
        #if check == self.pin :
            #amt = int(input("valid pin,enter the amount to be added :"))
        if not self.checkpin():
            return
        amt = int(input("valid pin,enter the amount to be added :"))
                            
        self.balance += amt 
        print("amount added successfully and the current balance is :",self.balance)
    def checkpin(self,checkpin=None):
        check = input("enter the pin to check :")
        if check == self.pin :

            print("valid pin")
            return True
        else :
            print("invalid pin !")
            return False
    def withdrawamount(self,amount):
        if not self.checkpin():
            return
        amt = int(input("enter the amount to be withdrawn :"))
        self.balance -= amt
        print("amount withdrawn successfully ! your current balance is :",self.balance)
    def displaybalance(self):
        if not self.balance :
            return
        else :
            print("your current balance is :",self.balance)
w1 = wallet()

w1.addingaccount(123456789012,"sai@12345")
w1.addamount(1000)
w1.displaybalance()
w1.withdrawamount(500)
w1.displaybalance()



