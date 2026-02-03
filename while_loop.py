def deposite(balance):
    amount=int(input("Enter the amount to deposite"))
    balance=balance+amount
    return balance
def withdraw(balance ,amount):
    balance-=amount
    return balance
def check_balance(balance):
    return balance
while True:
    print("welcome to the ATM")
    print("MENU")
    print("1.deposite")
    print("2.withdraw")
    print("3.check balance")
    print("4. EXIT")
    balance=10000
    choice=int(input("Enter your choice "))
    if choice==1:
       print(deposite(balance))
    elif choice==2:
       print(withdraw(balance))
    if choice==3:
       print(check_balance(balance))
    elif choice==4:
        print("thank you")
        break
        


