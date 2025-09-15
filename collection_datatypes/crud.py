import datetime

students=[{"id":1,"name":"alice"},{"id":2,"name":"john"}]

# students=[]



while True:
    print("\nwelcome to student management system\n")

    print("1. Read All student data")
    print("2. Add student data")
    print("3. update student data")
    print("4. delete student data")
    print("5. exit")


    choice = input("enter your choice ")

# read
    if(choice == "1"):
        if(students== []):
            print("No student data found")
        else:
            for s in students:
                print("id:",s["id"],"name",s["name"])

    elif(choice == "2"):
        id=len(students)+1
        # id = datetime.datetime.now().microsecond
        name= input("enter your name ")

        students.append({"id":id,"name":name})

        print("student data added")


    elif(choice == "3"):
        sId = int(input("enter student id to update "))

        for s in students:
            if(s["id"] == sId):
                 s["name"] =input("enter new student data to update ")
                 print("student data updated")
                 break
        else:
            print("student not found")    

    elif(choice == "4"):
        sId = int(input("enter student id to delete "))
        for s in students:
            if(s["id"]==sId):
                students.remove(s)
                print("student data deleted")
                break
        else:
            print("student not found")     

    elif(choice == "5"):
        print("good bye")
        break;       

    else:
        print("invalid choice, choose correctly")            




        


        

   




