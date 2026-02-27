#Question 39
#You are given a list of subjects for students.Assume one classrooom is for one subject.How many classrooms are needed by all students.

Subjects=["python","java","C++","python","javascript","java","python","java","C++","C"]
print(len(Subjects))
set_1={"python","java","C++","python","javascript"}
set_2={"java","python","java","C++","C"}
print(set_1.union(set_2))
print(len(set_1.union(set_2)))