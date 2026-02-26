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