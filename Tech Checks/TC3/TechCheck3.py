#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Taehong Min 
Program Title:  Grade Point Calculator
Description:    A console-based program that will take a letter grade
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    numericValue = 0.0
    gradeA = 4.0
    gradeB = 3.0
    gradeC = 2.0
    gradeD = 1.0
    gradeF = 0.0
    plusModifier = 0.3
    minusModifier = -0.3
    gradeWithModifier = 0.0
    finalGrade = 0.0

    print("Grade Point Calculator")
    print("\nValid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed  4.0.")

    #INPUT
    grade = input("\nPlease enter a letter grade : ").lower()
    modifier = input("Please enter a modifier (+, - or nothing) : ")

    #PRECESSING
    if grade == "a":
        numericValue = gradeA
        if modifier == "+":
            gradeWithModifier = numericValue
            print("\nThe numeric value is: {0}".format(gradeWithModifier))
        elif modifier == "-":
            gradeWithModifier = numericValue + minusModifier
            print("\nThe numeric value is: {0}".format(gradeWithModifier))
        elif modifier == "":
            gradeWithModifier = numericValue
            print("\nThe numeric value is: {0}".format(gradeWithModifier))

    elif grade == "b":
        numericValue = gradeB
        if modifier == "+":
            gradeWithModifier = numericValue + plusModifier
            print("\nThe numeric value is: {0}".format(gradeWithModifier))
        elif modifier == "-":
            gradeWithModifier = numericValue + minusModifier
            print("\nThe numeric value is: {0}".format(gradeWithModifier))
        elif modifier == "":
            gradeWithModifier = numericValue
            print("\nThe numeric value is: {0}".format(gradeWithModifier))

    elif grade == "c":
        numericValue = gradeC
        if modifier == "+":
            gradeWithModifier = numericValue + plusModifier
            print("\nThe numeric value is: {0}".format(gradeWithModifier))
        elif modifier == "-":
            gradeWithModifier = numericValue + minusModifier
            print("\nThe numeric value is: {0}".format(gradeWithModifier))
        elif modifier == "":
            gradeWithModifier = numericValue 
            print("\nThe numeric value is: {0}".format(gradeWithModifier))

    elif grade == "d":
        numericValue = gradeD
        if modifier == "+":
            gradeWithModifier = numericValue + plusModifier
            print("\nThe numeric value is: {0}".format(gradeWithModifier))
        elif modifier == "-":
            gradeWithModifier = numericValue + minusModifier
            print("\nThe numeric value is: {0}".format(gradeWithModifier))
        elif modifier == "":
            gradeWithModifier = numericValue   
            print("\nThe numeric value is: {0}".format(gradeWithModifier))

    elif grade == "f":
        numericValue = gradeF
        if modifier == "+":
            print("You entered an invalid letter grade.")
            print("The numeric value is: {0}".format(gradeWithModifier))
        elif modifier == "-":
            print("You entered an invalid letter grade.")
            print("The numeric value is: {0}".format(gradeWithModifier))
        elif modifier == "":
            gradeWithModifier = numericValue
            print("\nThe numeric value is: {0}".format(gradeWithModifier))
    
    else:
        print("You entered an invalid letter grade.")
        print("The numeric value is: {0}".format(finalGrade))
    

    #OUTPUT
    #print("\nThe numeric value is: {0}".format(finalGrade))




    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()