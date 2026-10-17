student = {"name": "Aarav", "age": 12, "grade": 7}
print(student)

print(student["name"])

student["school"] = "ABC School" #Add
student["age"] = 13 

for key in student :
    print("{} : {}".format(key , student[key]))

student.pop("grade") 
del student["age"] 
print(student)


student.clear()


print(student)