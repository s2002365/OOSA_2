
#########################
# An example of a class #
#########################

class yourBank(object):
  # an attribute
  numb_accounts=0
  # creation method
  def __init__(self,name,balance):
    print("Creating a class")
    self.name=name
    self.balance=balance
    yourBank.numb_accounts+=1
  # methods
  def deposit(self,amt):
    self.balance=self.balance+amt
  def withdraw(self,amt):
    self.balance=self.balance-amt
  def inquiry(self):
    return self.balance
  def tax(self,rate):
    self.balance=self.balance-self.balance*rate
