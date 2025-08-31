
# 🔹 List

# Definition: An ordered collection of items that is mutable (can be changed after creation).

# Syntax: my_list = [1, 2, 3, "apple"]

# Mutability: You can add, remove, or modify elements.

# mutable

fruits = ["apple","banana","mango"]


# add item in the end
fruits.append("banana")

print(fruits)


# add item at specific index

fruits.insert(2,"cherry")

print(fruits)


# add multiple item at once

fruits.extend(["strawberry","pineapple"])

print(fruits)

# remove

fruits.remove("banana")

print(fruits)

# remove the last element

fruits.pop()

print(fruits)

fruits.pop(2)

print(fruits)

del fruits[0]

print(fruits)

fruits.clear()

print(fruits)

number = [1,4,3,5]

print(number.index(4))


# count 

print(number.count(2))


#sort 


number.sort()
print(number)

#reverse 

number.reverse()

print(number)

copy_nums = number.copy()

print(copy_nums)

copy_nums[0] =5

print(copy_nums)