s={1,2,3}
#set
print(type(s))
print(s)
a=set()
print(type(a))
if 2 in s:
    print('yes')
else:
    print('no')
# for adding in set
s.add(10)
print(s)
# for removing in set
s.remove(2)
print(s)
#for discarding
s.discard(1)
print(s)

s.pop()
print(s)
#union
a={1,2,3,4,5,6,7,8}
b={3,4,5,6,7,8,9}
print(a|b)
print(a.union(b))

#intersection
print(a&b)
print(a.intersection(b))
#difference
print(a-b)
print(a.difference(b))
#symmetric differenec opposite of theintersection
print(s.symmetric_difference(b))
#users who logeed in this week

x={101,102,103,104,105,106}
#usrs who requested password resets
y={104,105,107}
#users flagged in asuspecious
z={103,108,105,110}
#find users who both looged in and requested a password
print('users both login and requesta pass',x.intersection(y))
#find users who done suspecioius activities but not logged in this week 
print('users done suspecious but not loged in',z-x)

#find users who do one of exactly one of 3 activities 
print( 'exactly one of three',(x ^ y ^ z) - (x & y & z))
#identify the users who were active in all of three 
print('active in all',x.intersection(y,z))

