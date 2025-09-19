

while True:

    print("welcome to bill Splitter app")

    totalBill = input("Enter total bill amount ")
    totalPeople = input("Enter total no of people ")
    tipPercentage=input("Enter tip percentage (0%,5%,10%,15%20%) ")


    if not totalBill.replace("."," ",1).isdigit() or not totalPeople.isdigit() or not tipPercentage.isdigit():
        print("invalid input please enter only numeric values")
        continue

    totalBill  = float(totalBill)
    totalPeople = int(totalPeople)
    tipPercentage= int(tipPercentage)


    if(totalPeople <=0):
        print("number of people must be greater then zero")
        continue
    if(totalBill <=0 or tipPercentage not in [0,5,10,15,20]):
        print("invalid bill amount and tip")
        continue


    tipAmount = (tipPercentage/100)*totalBill
    finalBill = totalBill+tipAmount
    splitAmount = finalBill/totalPeople


    print(f"tip amount is :Rupee {tipAmount}")
    print(f"Total bill with tip :Rupee{finalBill}")
    print(f"Each person should pay :Rupee {splitAmount}")


    anotherCalculate = input("\n would you like to calculate another bill ? (y/n): ").lower

    if(anotherCalculate != "y"):
        break

    print("thank you for using bill splitter app")





