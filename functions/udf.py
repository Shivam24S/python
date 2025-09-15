
# syntax of UDF 

def functionName(parameter):
    return

# optional  parameter, return value are optional


def greet():
    print("hello")

# invoking the function
# greet()    



# addition, function with parameter

# we are receiving parameter in function
def addition(x,y):
    result = x+y
    print(result)



# we are passing the argument
addition(10,2)   

addition(50,8)

addition(10,20)


# bank account example to understand default parameter


def createBankaAccount(name,amount=2000):
    print("account created",name,"and balance is ",amount )



createBankaAccount("john")



createBankaAccount("alice",5000)









