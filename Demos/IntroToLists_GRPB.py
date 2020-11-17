#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    
Program Title:  
Description:    
"""

def whateverFunc(x, y):
    print("whatever")
    return x

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    x = "KITTY"

    #Array --> List  <-- capable of holding multiple values at once    tuple    dictionary
    #Indexes   0        1       2        3          4
    pets = ["puppy", "kitty", "snake", "wombat", "hounddog"]

    # currentInstructor = [1, "Geoff", "Gillespie", "491-3035", "D311"]
    # currentInstructor2 = [2, "Mike", "Crocker", "491-3035", "D311"]

    # daysOfWeek = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    # print(len(pets))

    # for counter in range(5):
    #     print(str(counter + 1) + ": PET -", pets[counter])

    # # pets.append("platypus")
    # pets.insert(0, "bat")
    # print(pets.index(x.lower()))

    # print(pets)

    # print(daysOfWeek[4])

    guestList = []
    name = ""
    while name != "done":
        name = input("Enter your name: ")
        guestList.append(name)

    print(guestList)

    print("End")


    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()