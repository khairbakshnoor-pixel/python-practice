numbers=[]
odd=[]
even=[]
n=int(input("Enter the range"))
for i in range(n):
    elements=int(input("Enter the number"))
    numbers.append(elements)

for j in numbers:
    if j%2==0:
        even.append(j)
        
    elif j%2==1:
        even.append(j)
print(even )
print(odd)
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))   