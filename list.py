first = []
for i in range(1, 4):
    first.append(int(input("enter a number: ")))
print(first)
total = first[0] + first[1] + first[2]
avg = total / len(first)
print(avg)
count = 0
for i in first:
    if avg > i:
        count = count + 1
print(count)
