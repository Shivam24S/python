

number = [10,50,6,0,70,80,40]

print("array or list",number)


# add

number.append(70)

print("new element added in array",number)


# insert


number.insert(2,24)

print("array or list",number)


# extend


number.extend([0,0])
print("array or list",number)


# remove


number.pop()

print("array or list",number)


number.pop(0)

print("array or list",number)

# remove 

number.remove(24)

print("array or list",number)


# update 


number[0]=100

print("array or list",number)


# access

print(number[0])


# sort


number.sort()

print("sorted",number)

# descending

number.sort(reverse=True)

print("descending",number)


# max 



print("max value",max(number))

# min


print("min value",min(number))

# count

print("count 0 :",number.count(0))

# index

print("index",number.index(0))


