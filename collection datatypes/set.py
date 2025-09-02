

# set is un order collection of unique elements


number={1,2,3,1,2,3,4,5,6}


print("removing the duplicate",number)



number.add(7)

print("adding element to set",number)

# remove

# number.remove(6)

# print("removing the element",number)

# will generate error 
# number.remove(6)

# print("removing the element",number)


# 

number.discard(6)

print("discarding number if not error will not generate",number)


removedNum = number.pop()

print("removed number",removedNum)

print("all",number)


# clear

number.clear()

print("clear",number)



# other operation


num1={1,2,3}

num2={3,4,5}


# union
print("will remove the duplicate and return whole joint set",num1.union(num2))

# intersection (common in both)

print("common in both set",num1.intersection(num2))

# difference

print("difference",num1.difference(num2))

# symmetric difference

print("symmetric diff",num1.symmetric_difference(num2))