from bank_account import BankAccount #from file name import class name


account = BankAccount("1253592", 1000)
print(account)

account.deposit(300)
print(account)

account.withdraw(500)

print(account.get_balance())

account2 =  BankAccount("123456", 10000000)
print(account)
account2.deposit(100000)
account2.withdraw(2000)
print(account2.get_balance())
