#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    
Program Title:  
Description:    
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    guestList = []
    paidAmountList = []

    #Ask how money was spent on snacks/beer/etc?
    partyCost = float(input("How much money was spent on party supplies? $"))

    #Each guest owes their part of the party bill      (Divide party cost by number of guests to split the bill evenly)
    # numOfGuests = int(input("How many people are you inviting? "))

    # costPer = partyCost / numOfGuests
    # print("Cost per guest: ${0:.2f}".format(costPer))

    #Use a loop to gather 3 names from the user, and add them to a list
    while True:
        name = input("Please enter a name (enter done when finished): ")
        if name.lower() == "done":
            break
        # else:
        total = float(input("How much are you paying? $"))
        guestList.append(name)          #Example of using parallel lists
        paidAmountList.append(total)       #Ditto

    print(guestList)            #Example of using parallel lists
    print(paidAmountList)       #Ditto

    for i in range(len(guestList)):
        print("Guest ", guestList[i], "paid ${0:.2f}".format(paidAmountList[i]))

    # costPer = partyCost / len(guestList)  #When the cost was shared by ALL (before free Matts)
    numOfMatts = 0
    #Loop through the values added to the list (see prev code) and print them one at a time
    # for i in range(len(guestList)):
    #     if guestList[i].lower() == "matt":
    #         print(guestList[i], "is invited to my party. They owe $0")
    #         numOfMatts += 1
    #     else:
    #         print(guestList[i], "is invited to my party.")         #0  1   2

    #Example of stepping through a list that has name cost name cost name cost pattern
    # totalPaid = 0
    # for i in range(1, len(guestList), 2): #Use range function to start at second value and skip by twos
    #     totalPaid += guestList[i]
    # print(totalPaid)

    #One way: Use the .count() function for lists
    #numOfMatts = guestList.count("Matt")

    costPer = partyCost / (len(guestList) - numOfMatts)

    #How many names in the list?
    print("Number of guests: {0} and they each owe ${1:.2f} (Matts are free)".format(len(guestList), costPer))

    #Preview of upcoming code
    # .split()      .join()     <-- functions that change from a list to a string or vice versa

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()