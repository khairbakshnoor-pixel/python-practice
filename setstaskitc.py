colors={'red','green',"red",'blue'}
print(colors)
colors.add("yellow")
print(colors)
colors.update(["purple","pink"])
print(colors)
#remove the item if item is not present in the list it willgive error
colors.remove("pink")
print(colors)
#discard remove the itenm also giving no any error if the item is not present inm the list
colors.discard("Yellow")
print(colors)
colors.clear()
print(colors)