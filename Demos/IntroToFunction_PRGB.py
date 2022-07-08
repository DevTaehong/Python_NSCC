#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    
Program Title:  
Description:    Program that asks   user to enter a decimal value, build a function
                that will always round up (ceiling rounding)
"""

def roundToCeiling(numToRound):
    #This function will include any code that is used when we round to ceiling
    roundedNum = numToRound

    #Rules of how to round? Use int()?
    if int(numToRound) < numToRound:
        roundedNum  = int(numToRound) + 1

    return roundedNum
    #print("Your CEILING rounded number is: {0}".format(roundedNum))

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #Ask user to enter a decimal number
    userNumber = float(input("Please enter a decimal number: "))

    #Build a function that does ceil rounding
    #Function definition - Don't define a function inside another function!

    #Pass the user's number to our function
    #Function call
    finalAnswer = roundToCeiling(userNumber)

    #Display the newly rounded number
    print("Your number, with ceiling rounding, is: {}".format(finalAnswer))


    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()  #<-- THIS IS A FUNCTION CALL TOO!