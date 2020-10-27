#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Taehong Min 
Program Title:  Landscape Calculator
Description:    Making a program that computes the price of landscapeing
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #Variables and Initializing 
    labourCharge = float(1000)
    overSquare = float(5000)
    typeGrass = "" 
    totalCost = 0.0
    costFescue = 0.05
    costBentgrass = 0.02
    costCampus = 0.01
    overCost = float(500)
    cost = 0.0
    treeCharge = float(100)

    #INPUT
    #Input Messages
    houseNum = input("Enter House Number: ")
    depth = int(input("\nEnter property depth (feet): "))
    width = int(input("\nEnter property width (feet): "))
    typeGrass = input("\nEnter type of grass (fescue, bentgrass, campus): ").lower() #for lower case
    treeNum = float(input("\nEnter the number of trees: "))

    #PROCESSING
    #Calculate surface value!
    surface = float(width * depth)

    #Decision among fescue, bentgrass, campus and then calculating!
    if typeGrass == "fescue":
        #over 5000 square feet, add $500
        if surface > overSquare:
            cost = surface * costFescue + overCost
        #under 5000, no add $500
        else:
            cost = surface * costFescue

    elif typeGrass == "bentgrass":
        #over 5000 square feet, add $500
        if surface > overSquare:
            cost = surface * costBentgrass + overCost
        #under 5000, no add $500
        else:
            cost = surface * costBentgrass

    elif typeGrass == "campus":
        #over 5000 square feet, add $500
        if surface > overSquare:
            cost = surface * costCampus + overCost
        #under 5000, no add $500
        else:
            cost = surface * costCampus

    #Calculate total cost according to decision!!!!
    totalCost = cost + labourCharge + (treeNum * treeCharge)

    #OUTPUT
    print("\nTotal cost for house {0} is: ${1:.2f}".format(houseNum, totalCost))

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()