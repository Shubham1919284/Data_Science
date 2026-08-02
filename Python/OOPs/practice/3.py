class BankAccount:
    def __init__(self):
        self.__balance=0  # Private attribute

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        return self.__balance

    def withdraw(self,amount):
        if amount>0 and amount<=self.__balance:
            self.__balance-=amount
        return self.__balance

    def get_balance(self):
        return self.__balance

    def set_balance(self,amount):
        if amount>=0:
            self.__balance=amount
        return self.__balance

user=BankAccount()
print(user.get_balance())  # Output: 0
user.deposit(100)
print(user.get_balance())  # Output: 100
user.withdraw(50)   
print(user.get_balance())  # Output: 50
user.set_balance(20000000) # This will set the balance to 20000000 and shows us how encapsulation works in python as we are not able to access the private attribute directly but we can access it through the public methods of the class.
print(user.get_balance())  # Output: 20000000