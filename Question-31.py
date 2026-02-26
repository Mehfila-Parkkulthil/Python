#Question 31
#Write to check if a list contains palindromic of elements

my_list=[1,2,"abs","biceps","abs",2,1,0]
list_copy =my_list.copy()
list_copy.reverse()
if(my_list==list_copy):
  print("Its a palindrome")
else:
  print("not a palindrome")