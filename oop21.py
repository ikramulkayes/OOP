#Write your code here
class BankAccount:
    def __init__(self,id,name,pin,money):
        self.id = id
        self.name = name
        self.pin = pin
        self.money = money
        print("Account Number:",self.id)
        print("Account Name:",self.name)
        print("Pin:",self.pin)
        print("Total Balance:",self.money)
    def deposit(self,dep):
        self.money += dep
        print(f"After deposit of {dep} the Total Balance in the account is {self.money}.")
    def withdraw(self,wit):
        self.money -= wit
        print(f"After withdrawal of {wit} the Total Balance in the account is {self.money}.")





# TODO

#Do not change the following code:
Tom_Holden = BankAccount("234729920000034", "Tom Holden", 45879, 7854124)
Tom_Holden.deposit(34000)
Tom_Holden.withdraw(2145000)