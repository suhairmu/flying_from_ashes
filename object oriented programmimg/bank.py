'''
bank

bname
acc no
balance
createaccount()
deposit()
withdrawl()
balEnq()
'''

import datetime
class Bank:
    bname="sbi"
    def createAccount(self,bname,accno,balance):
        #self.bname=bname
        self.accno=accno
        self.balance=3000

    def deposit(self,amt):

        self.balance+=amt

        print("your ",Bank.bname,"account has been credited with amount",amt)   #static variable can invoke by class name also (Bank,bname)
        print("on ",datetime.datetime.now(),"current balance=",self.balance)

    def withdraw(self,amt):
        if(amt>self.balance):
            print("insufficient fund")
        else:
            self.balance-=amt   #self.balance=self.balance-amt
            print("your ", self.bname, "account has been debited with amount", amt)
            print("on ", datetime.datetime.now(), "current balance=", self.balance)
    def balanceEnq(self):
        print("your account balance =",self.balance)


obj=Bank()
obj.createAccount("sbi",1003,1000)
obj.withdraw(500)
obj.balanceEnq()