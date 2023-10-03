#create a tuple
tuplex = "1", "2", "3", "4", "5", "6", "7", "8", "10"
print(tuplex)
#tuples are immutable, so you can not remove elements
#using merge of tuples with the + operator you can remove an item and it will create a new tuple
tuplex = tuplex[:2] + tuplex[3:]
print(tuplex)
#converting the tuple to list
listx = list(tuplex) 
#use different ways to remove an item of the list
listx.remove("8") 
#converting the tuple to list
tuplex = tuple(listx)
print(tuplex)
