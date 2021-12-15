import random
class Account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + "-" + num2 + "-" + num3
shin = Account("신승수",100)
print(shin.name)
print(shin.balance)
print(shin.bank)
print(shin.account_number)