numbers=[]
positive=[]
negative=[]
n=int(input("Enter number of elements in list"))
for i in range(n):
    element=int(input("Enter the element"))
    numbers.append(element)

for num in numbers:
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)

print("Positive numbers:", positive)
print("Negative numbers:", negative)
