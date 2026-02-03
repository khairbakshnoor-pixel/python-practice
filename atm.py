# 1. ATM management system 
# 2. Input list, check for each element weather 
# is it positive or negative, store &
# display both in different lists

balance=10000
def deposite(amount):
        
        global balance
        balance+=amount
       
def withdraw(amount):
        if amount<balance:
         global balance
         balance-=amount
        else:
            print("insufficient balance")
       
def show_balance():
        global balance
        print(balance)
while(True):
    print("welcome to ATM ")
    print("MENU")
    print("1.deposite MONEY ")
    print("2.withdraw MONEY")
    print("3.show balance")
    print("4. exit")
    
    choice=int(input("Enter your choice     :"))
    if choice==1:
     amount=int(input("Enter the amount you want to deposite"))
     deposite(amount)
    elif choice ==2:
       amount=int(input("enter amount you want to withdraw"))
       withdraw(amount)
    elif choice==3:
       show_balance()
    elif choice==4:
       break
    else:
       print("invalid choice")