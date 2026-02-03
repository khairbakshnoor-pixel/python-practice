a=int(input("enter the number       "))
sum=0
for i in range (0,a+1):
    sum=sum+i
    print(i)
print('the sum of first',a, 'natural number is=',sum)
for j in range(0,a+1,2):
    sum=sum+j
    print(j)
print('the sum of first ',a,'even numbers is=',sum)

