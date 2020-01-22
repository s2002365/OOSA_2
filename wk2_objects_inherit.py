from wk2_objects import yourBank

class badBank(yourBank):
    '''this class inherits the attributes and methods from yourBank class but adds some more functions '''
    def deposit_plus_vat(self, amt): #function adds a user defined balance (plus 20% vat)
        self.balance=self.balance+amt*1.2



'''
#STEVES CODE

#############################
# An example of inheritance #
# and overloading           #
#############################

# import previous class definition and random number generator
import myBank
import random


# new classes, inheriting from yourBank

class evilBank(myBank.yourBank):
  # overload the inquiry operator
  def inquiry(self):
    if(random.random()>0.66666):
      return self.balance*1.1   # David M. Beazley, 2009
    else:
      return self.balance
'''
