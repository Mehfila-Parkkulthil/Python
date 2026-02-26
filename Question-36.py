#Question 36
#Nested Dictionaries

Student={
  "name" :"Jack",
  "score" :{
    "chem" : 98,
    "phy"  : 65,
    "bio"  : 90
    }
}

Student["score"]["math"] = 87
print(Student)
print(Student["score"]["math"])