class BankAccount:
    def __init__(self, account_number, balance):
      #the two underscores privates and secures the data below
      self.__account_number = account_number
      self.__balance = balance
     
    @property
    def set_account_number(self, account_number):
        self.__account_number = account_number
      
    def get_account_number(self):
        return self.__account_number
        
    # this checks whether the value that will be used to change is negative
    @property
    def set_balance(self, balance):
        if balance > 0:
            self.__balance = balance
            
    def get_balance(self):
        return self.__balance
        
a1 = BankAccount(12345, 1000)

print("Account 1")
print("Account Number: ", a1.get_account_number())
print("Balance: ", a1.get_balance())

print("Update balance to -100")
print("The balance must not be a negative number")
print("Account Number: ", a1.get_account_number())
print("Balance: ", a1.get_balance())
