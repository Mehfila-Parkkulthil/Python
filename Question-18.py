#Question 18
#Conditional statements
#Can vote or not

name=input("Name:")
age=int(input("Age:")) #input always written a str
if(age>18):
  print(name , ", You can vote")
else:
  print(name, ", You cannot vote")
