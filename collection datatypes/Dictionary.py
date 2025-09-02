
# # Collection of key-value pairs.

# student = {"name":"alice","age":20}


# # access

# print(student["name"])

# print(student.get("age"))

# # add property

# student["grade"]="A"

# print(student)

# # update 

# student["age"] = 25

# print(student)

# student.update({"age":"21"})

# print(student)


# # remove

# student.pop("grade")

# print(student)

# del student["age"]
# print(student)

# # student.clear()
# print(student)


# print(student.keys())

# print(student.values())

# print(student.items())































student = {"name":"alice","age":"20"}


# access

print(student["name"])

print(student.get("age"))

# add

student["grade"] = "a"

# update 

student["grade"]="b"

student.update({"age":22})

# remove

student.pop("grade")


del student["age"]


# student.clear()

print(
student.keys())

print(student.values())

print(student.items())

print(student)