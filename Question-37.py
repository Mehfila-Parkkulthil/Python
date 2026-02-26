#Question 37
#Dictionary methods

my_dict={
  "age" :23,
  "age_present" : 32
}
print(my_dict.values())#values as list
print(my_dict.keys())#keys as list
print(my_dict.items()) #gives key value pairs as tuple
print(my_dict.get("age"))#return the key according to value
print(my_dict.update({"key":"values"}))
print(my_dict)
