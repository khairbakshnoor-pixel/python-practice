def fact(n):
    if(n<=0):
        return 1
    else :
        return n*fact(n-1)
n=int(input("enter a number "))
print("the factorial of the number is ",fact(n))