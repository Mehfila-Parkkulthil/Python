#Question 29
#Write a program to ask the user to enter name of their three favourite movies and store them in a list

movies=[]
#list are defined square brackets
#yes you can create list without brackets but not like tuple instead, list() , eg: a=list((1,2,3)) i,e. convert tuple to listand a= list("hello").List are mutable unlike tuple

# [] → list

# () + comma → tuple

# comma alone → tuple

# parentheses alone → just grouping

print(movies)
print("So your movies box is empty")
# movies[0]=input("Pls write your  second favourite movie : ")
# movies[1]= input("Pls write your  first favourite movie : ")
# movies[2]=input("Pls write your  second favourite movie : ")
# shows error as they are emptyy list or donot exist and You can only assign to an index that already exists. List must have space first.yet so

movies.append(input("First favourite movie: "))
movies.append(input("Second favourite movie: "))
movies.append(input("Third favourite movie: "))
print(movies)
print("Thank you")
# or 
# movies = ["", "", ""]
# movies[0] = input("First favourite movie: ")
# movies[1] = input("Second favourite movie: ")
# movies[2] = input("Third favourite movie: ")

# print(movies)