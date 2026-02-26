#Question 27
#List methods

Let_list=[23,12,78]
Let_list.append(4)#add one element at the end
print("append - " , Let_list)
Let_list.sort()#sort in ascending and descending order
print("sort - " , Let_list)
Let_list.sort(reverse=True)#reverse the order 
print("reverse -" ,Let_list)
Let_list.reverse()
print("reverse - " ,Let_list)
Let_list.insert(2,36)#adds 36 to second index but doesnt remove anything
print("insert - ",Let_list)
Let_list.remove(4) #remove the first occurance of the element
print("remove - ", Let_list)
Let_list.pop(3)#remove the element at the mentioned index here, 3
print("pop - ",Let_list)