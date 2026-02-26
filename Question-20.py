#Question 20
#marks>=90 - grade A
#90>marks>=80 , grade B
#80>marks>=70, grade C
#70>marks, grade D

print("Grade calculator")
marks=int(input("Enter your marks:"))
if(marks>100):
  print("invalid, marks are out of 100")
elif(marks>=90):
  print("Wohoo!! Grade A")
elif(90>marks>=80):
  print("Congrats, Grade B")
elif(80>marks>=70):
  print("Good, Grade C")
elif(70>marks):
  print("Work hard, Grade D")
else:
  print("invalid")