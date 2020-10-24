#Paint Shop Calculator
#Program to calculate the number of gallons of paint required to paint a room, if provided the room dimensions

#Import the math class, for using ceiling rounding
import math

def areaOfWall(lenth, width, height):
    totalAreaInFunction = (length * height * 2) + (width * height * 2)
    print("\nThe total wall area of your room is {0} square feet.".format(totalAreaInFunction))
    return totalAreaInFunction 

def gallons_of_paint(totalAreaInSecondFucntion):
    square_feet_per_gallon = 150.0
    gallons_of_paintInFucntion = math.ceil(totalAreaInSecondFucntion / square_feet_per_gallon)
    print("You will need {0} gallon(s) of paint. \n\nHappy Painting!".format(gallons_of_paintInFucntion))
#Declare variable for # of sq. ft. covered by one gallon of paint

#Intro messages
print("Welcome to the Paint Shop!")
print("This program will help you calculate how many cans of paint you need to buy, based on the dimensions of your room.")

#INPUT
#Get Dimensions of the room
length = float(input("\nEnter the length of the room, in feet: "))
width = float(input("Enter the width of the room, in feet: "))
height = float(input("Enter the height of the room, in feet: "))

totalArea = areaOfWall(length, width, height)
gallons_of_paint(totalArea)
#PROCESSING
#Calculate the area of the walls


#Divide the area by 150 square feet and
#round number of gallons up to the nearest whole number


#OUTPUT - Display number of gallons needed


