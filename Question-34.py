#Question 34
#Dictionaries 

dictionary ={
  "name" : "Mehfila Parkkulthil",
  "age" : 24.7,
  "cgpa" : 7.0,
  "marks" :[98,34,87],
}
dictionary["name"] = "Aiera Parkkulthil" # to rewrite key value
print(dictionary)
print(type(dictionary))
print()
print(dictionary["age"]) #only prints values
print()
print(dictionary["marks"])#only prints values

#values can be of any datatypes .
#keys can be boolean ,tuple or string all immutable are okay.
#keys cant be list
#keys can float or int.

info= {
  91 : 6234234645
}
print(info)
print(type(info))
print(info[91])
info["surname"] = "file" #key is str
info[True]="Teacher" #key is bool
info[(1,2,3)]=(23,32,12) #key is tuple
info[12]=[23,"name"] #value is list
print(info)
print()
# info[[12,23,12]] ="listkey" - shows error