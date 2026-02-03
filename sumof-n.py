n=int(input("enter a number     :"))
sum=0
for i in range (1,n+1):
    if i%2==0:
        sum=sum+i
print(sum)
for a in range (1,6):
    for j in range (1,a+1):
     print(j,end=" ")
    print()