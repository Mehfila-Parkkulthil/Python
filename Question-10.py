#Question 10
#Dictionaries

info = {
  "name" : "Mehfila Pakkulthil",
  "age" : 24,
  "Education" : "Graduate",
  "subject" : ["Physics", 'Maths', "Chemistry","Computerscience" ], #list
  "Place" : ("Bangalore",'Calicut'), #tuple
  "Personal-curicculum" :["Ecommerce" , "Entreprenuership","Marketing"],
  "Marks":{#nested dict
    "Graduation":77,
    "Curriculum":89,
  }
}
print()
print(info.keys())
print()
print(info.values())
print()
print(list(info.values()))
print()
print(info.items())
print()
print(list(info.items()))
print()
pairs=list(info.items())
print(pairs[0])
print()
print(info["name"])
print(info.get("name"))
#print(info["name"]) #gives error
#print(info.get("name")) #gives none
print()
info.update({"city" : "Tvm"})
new_dict={"fav-city":"Calicut"}
info.update(new_dict)
print(info)
info.update({"name":"Aiera"})#name gets updated as duplicates are not allowed in dict
print()
print(info)