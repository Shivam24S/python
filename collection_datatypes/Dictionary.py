
# key value pair 


student = {"name":"alice","age":22}


# access

print(student["name"])


print(student.get("age"))


# add

print(student)

student["grade"] = "A"

print(student)


# update

student["grade"] = "b"

print(student)


student.update({"age":24})


print(student)

# delete


del student["grade"]

print(student)


# student.clear()

# print(student)


# 

print(student.keys())

print(student.values())

print(student.items())