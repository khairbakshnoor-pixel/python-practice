#Create a tuple of 5 numbers and print the maximum and minimum values.
a=(1,2,3,4,5)
print(type(a))
print(max(a))
print(min(a))
#Convert a tuple into a list, add an item, and convert it back to a tuple
b=('tuple','list','dictionary','set')
print(type(b))
b=list(b)
print(type(b))
b.append('tuple to list')
print(type(b),b)
print(b)
b = tuple(b)  # convert back to tuple
print(type(b), b)
print(b.count)
#for printing without commas
print(*a,sep="\n")
areeb=('areeb','ahmed','khan',6,5,7)
print(areeb)
s="areeb 1 ,2 "
print(s)