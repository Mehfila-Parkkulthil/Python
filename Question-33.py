# Question 32
#Write a program to sort the grades of students in the following tuple

#list can be sorted but tuple cant be

tuplle=("C","A","D","A","F","B","A","A","A","C","D")
# t.sort()-shows Error
#but sorted()works
# t = (5, 2, 9, 1)
# sorted_t = sorted(t)
# print(sorted_t)
# [1, 2, 5, 9] -result will be a list
# For tuple result
# sorted_t = tuple(sorted(t))
# print(sorted_t)
sorted_t=tuple(sorted(tuplle))
# tuple(  [sorted list]  )
print(tuplle)
print()
print(sorted_t) #gives tuple
print()
print(tuple)
print()
sorted(tuplle) #gives list
print()
print(type(sorted(tuplle)))           # list
print(type(tuple(sorted(tuplle))))    # tuple


# Original tuple
#       ↓
# sorted() → list
#       ↓
# tuple() → tuple