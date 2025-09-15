# function are used to reuse the same logic often in whole program

# using function we are following DRY (Do not repeat yourself)  principal

# print function is used to log the output

print("hello")


# input function is used to take input from user

# input("enter something")



# to check length we are using len 

word = "python"

print("length od the word",len(word))


number=[10,5,8,9,6,3,7,1]

print("sorted number are in ascending order",sorted(number))


# descending order

print("reversed",sorted(number,reverse=True))


# # sum method used to perform addition

# num1=10

# num2=20

# # result =  sum(num1+num2)

# print("total of two  number",result)


# type 

greet="hello"

print("type of greet",type(greet))


num=10

print("type of num",type(num))


# type casting used for convert data to other data type


# int() convert to decimal number

num="10"

print("type of num",type(num))


newNum = int(num)


print("type of num",type(newNum))


# integer to  float


num=10

print("type of num",type(num))



decimalNum = float(num)

print("type of decimalNum",type(decimalNum))



scores = [10,20,50,40,9,80,70,90]

print("max scores",max(scores))


# minimum find the minimum value

print("minimum scores",min(scores))






# range (start,end,step) , end is exclusive will not count 

# for i in range(1,5):
#     print(i)







# deep copy (by value )


a=5

b=a

print(a)

print(b)

b=10

print(a)



# shallow copy  (by reference)


number1= [1,5,6,45,5,5]

# print(number1)

number2=number1

number2[0]=10

print(number1)