#Question 17
#string funcitons

str="I am a coder"
#str.endswith checks if the string ends with the substring
check_od=str.endswith('od')
check_er=str.endswith("er")
print(check_od)
print(check_er)

#str.capitalise, capitalises the first character of the str
str_new="i love myself"
print(str_new.capitalize())

#str.replace(old,new), replaces all ocurences with new.
string_new ="i hate myself"
print(string_new.replace("hate","love"))

#str.find(word),returns first index of first occurance
print(str.find("coder"))
print(str.find("mine"))
#Returns -1 if not found and if found , returns the index of first occurence
#find() → safe, returns -1
#indexing → unsafe, may crash

#str.count(word), counts the occureance of substr in a str(ie, each word appears how many times)
print(str_new.count("love"))
print(str_new.count("myself"))