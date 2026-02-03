def total(*number):#        *numbers is for n 
    print(sum(number))
total(5,10)
total(6,6,44,20,14)
#args==variable number of positional arguments
#keywords args ==variable number of keyword argument,,kwargs
def data(**details):
    for k ,v in details.item():
     print(k,'=',v)
data(name='ali',age=18,clas=5)
data()


