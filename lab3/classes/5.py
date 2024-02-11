#Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals may not exceed the available balance. 
#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, sum):
        self.balance += sum
        print("Your balance is", self.balance)

    def withdraw(self, sum):
        if sum > self.balance:
            print("You cannot overdraw your balance.")
            return False
        elif sum < self.balance:
            self.balance -= sum
            print("Updated balance:", self.balance)
            return True
        elif sum == self.balance:
            self.balance = 0
            print("Your balance is empty.")

account = Account(str(input("Your name: ")), int(input("Initial bank balance: ")))
account.deposit(int(input("Deposit sum: ")))
account.withdraw(int(input("Withdraw sum: ")))

#done