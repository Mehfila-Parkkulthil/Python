#Question 41
#Write a program to enter marks of 3 subjects from the user and store them in a dictionary.Start with an empty dictionary and add one by one.Use subject name as key and marks as value

my_dictionary = {}
print(my_dictionary)
maths=int(input("Enter your maths mark:"))
physics=int(input("Enter your physics mark:"))
chemistry=int(input("Enter your chemistry mark:"))

my_dictionary["maths"]= maths
my_dictionary["physics"]= physics
my_dictionary["chemistry"]= chemistry
print(my_dictionary)