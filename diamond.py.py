n=5
for  i in range(1,n+1):
    for j in range (n - i):
        print(" ", end=" ")
    for k in range (2*i-1):
          print("*",end=" ")
    print()
for  l in range(5,1,-1):
    for h in range (5-l):
        print(" ", end=" ")
    for c in range (2*l-1):
          print("*",end=" ")
    print()