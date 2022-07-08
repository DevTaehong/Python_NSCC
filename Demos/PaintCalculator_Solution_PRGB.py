#Paint Shop Calculator
#Program to calculate the number of gallons of paint required to paint a room, if provided the room dimensions

#Import the math class, for using ceiling rounding
import math

X = 123

def showIntro():    #This function shows the intro print messages
    print("Welcome to the Paint Shop!")
    print("This program will help you calculate how many cans of paint you need to buy, based on the dimensions of your room.")

def GetAUserInput(dimensionName):    #Function to ask user for input and change it to float
    userInput = float(input("\nEnter the " + dimensionName + " of the room, in feet: "))
    return userInput

def calcTotalAreaOfARoom(prm_length, prm_width, prm_height):
    answer = (prm_length * prm_height * 2) + (prm_width * prm_height * 2)
    return answer

def geoffsPaintShop():
    #Declare variable for # of sq. ft. covered by one gallon of paint
    square_feet_per_gallon = 150.0

    #Intro messages
    showIntro()

    #INPUT
    #Get Dimensions of the room
    length = GetAUserInput("length")
    width = GetAUserInput("width")
    height = GetAUserInput("height")

    #PROCESSING
    #Calculate the area of the walls
    totalArea = calcTotalAreaOfARoom(length, width, height)

    #Divide the area by 150 square feet and
    #round number of gallons up to the nearest whole number
    gallons_of_paint = math.ceil(totalArea / square_feet_per_gallon)

    #OUTPUT - Display number of gallons needed
    print("\nThe total wall area of your room is {0} square feet.".format(totalArea))
    print("You will need {0} gallon(s) of paint. \n\nHappy Painting!".format(gallons_of_paint))

geoffsPaintShop()













