def main():
    #INPUT -- Two sets of walls and height of the room
    
    print("The Paint shop")

    TheWidthOfWalls = input("Please enter the width of your two sets of walls: ")
    TheHeight = input("Please enter the height of the room: ")
    Feet = 150
    #PROCESSING
    
    TheNumberOfGallons = int(TheWidthOfWalls) * int(TheHeight)
    Gallons = TheNumberOfGallons * Feet

    #OUTPUT - the number of gallons 

    print("The amount of paint you need is:",Gallons)
main()