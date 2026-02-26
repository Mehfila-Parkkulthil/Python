#Question 28
#Tuples in python

tuple =(78,34,98,32,12,3,6,32,45,42,32)
print(tuple[2])
# tuple[0]=33 shows error tuples are immutable

tuple_new =() #empty tuple
print(tuple_new)

tuple_new=(1,)#type is tuple with comma
print(tuple_new)

tuple_new=(1,2,3) #type is tuple with comma
print(tuple_new)
print(type(tuple_new))

tup=(1) #with no comma type is int
print(type(tup))

tupll=(2.3)#with no comma type is float
print(type(tupll))

print(tuple.index(3)) #shows the index number were number 3 occurs in tuple here 3 is in fifth position

print(tuple.count(32)) #counts how many times 32 appears

print(len(tuple))

#print(len(tup)) -shows error

#print(len(tupll)) -shows error

tuple_str=("hello")  #str type not tuple
print(tuple_str)
print(type(tuple_str))
print(len(tuple_str))
print(tuple_str[3])

tuple_new_str ="Aiera" #str type not tuple
print(type(tuple_new_str))

tuple_num = 22,34,32
print(tuple_num)
print(type(tuple_num))

tuple_dupe=("name","aiera","jack")
print(tuple_dupe)
print(type(tuple_dupe))
# Important_note : In python comma creates a tuple not paranthesis.Parenthesis are more for readability.