
#users who logged in this week
A = {101, 102, 103, 104, 105, 106}
print(*A)
A.add(107)
    #"Users who requested password resets\n",
    
B = {104, 105, 107}
   # "Users flagged in a suspicious activity\n",
    
C = {103, 108, 105, 110}
#Find the users who both logged in and requested a password reset
print(A.intersection(B))

#find users who triggered suspicious activity but did not login this week
print(C.difference(A))

#find users who did exactly one of 3 activities
print((A - B - C).union(B - A - C).union(C - A - B))

#identify users who were active in all 3 lists
print(A.intersection(B).intersection(C))
