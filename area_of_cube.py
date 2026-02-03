def area_of_sqr(l):
          return l*l
def area_of_cube(s):
        base=area_of_sqr(s)
        return 6* base
area=area_of_sqr(6)
print("area of sqr",area)

area_of_cube=area_of_cube(6)
print(area_of_cube)