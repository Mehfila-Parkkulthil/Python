#Question 8
#Create a list stuffs

names =['Aiera','Savaf', 'Mehfila']
print("Given list - ") 
print(names)

names.append('Ifna')
print(names)

names.pop(2) #delete index number 2
print(names)

names.insert(2,'Hanan') #adds hanan at position 2
print(names)

names.remove('Hanan')#removes hanan
print(names)

del names[2:]
print(names)

names.clear
print(names)