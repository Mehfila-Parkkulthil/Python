#Question 22
#Write a program to find the greatest of 3 numbers entered by the user

first = int(input("Enter your first number:"))
second = int(input("Enter your second number:"))
third =int(input("Enter your third number:"))
if(first>second and first>third):
  print("First is greatest")
elif(second>third and second>first ):
  print("Second is greatest")
else:
  print("third is the largest")