

number = [1,2,8,7,6,5,4,3]

print(number)

# add methods 


number.append(10)

print(number)


# insert 

number.insert(4,20)

print(number)

# extend

number.extend([30,40])

print(number)


# remove 

number.pop()

print(number)


number.pop(3)

print(number)


# remove

number.remove(10)

print(number)


# del

del number[0]


print(number)


# clear

# number.clear()


# print(number)

# update 

number[0]=100

print(number)


# sort

number.sort()

print(number)


# descending order

number.sort(reverse=True)

print(number)






# exercise


vegetables = ["potato","tomato","ginger","lemon"]


print(vegetables)


# adding 4 vegetables


vegetables.extend(["lady-finger","onion","cabbage","brinjal"])


print(vegetables)


# i want to count how many elements in list

print(len(vegetables))


# i want to delete ginger from my list

vegetables.remove("ginger")

print(vegetables)


# sort

vegetables.sort()

print(vegetables)


# reverse

vegetables.sort(reverse=True)


print(vegetables)


# update


vegetables[2] = "carrot"

print(vegetables)




