#Question 42
#Write a program to enter marks of 3 subjects from the user and store them in a dictionary.Start with an empty dictionary and add one by one.Use subject name as key and marks as value

my_dictionary = {}
print(my_dictionary)
maths=int(input("Enter your maths mark:"))
my_dictionary.update({"maths":maths})
physics=int(input("Enter your physics mark:"))
my_dictionary.update({"physics":physics})
chemistry=int(input("Enter your chemistry mark:"))
my_dictionary.update({"chemistry":chemistry})
print(my_dictionary)

# .update() is more useful when:

# Adding multiple key-value pairs at once

# Merging two dictionaries