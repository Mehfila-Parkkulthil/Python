#Question 30
#Write to check if a list contains palindromic of elements

list=[1,2,3,4,3,2,1]
copy_list =list.copy()
copy_list.reverse() #reversed copy_list
if(list==copy_list):
  print("its palindrome")
else:
  print("not")