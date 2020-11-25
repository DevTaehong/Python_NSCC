############################################
# Tech Check 4 - Provided Starter File
############################################
def main():
    
    courseName = ["PROG1700", "NETW1700", "OSYS1200", "WEBD1000", "COMM1700", "DBAS1007"] 
    
    print("Grade Point Calculator\n")
    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0.\n")

    
    FunNumericGrade1 = fucCalculator(courseName[0])
    FunNumericGrade2 = fucCalculator(courseName[1])
    FunNumericGrade3 = fucCalculator(courseName[2])
    FunNumericGrade4 = fucCalculator(courseName[3])
    FunNumericGrade5 = fucCalculator(courseName[4])
    FunNumericGrade6 = fucCalculator(courseName[5])

    averageGrade = (FunNumericGrade1 + FunNumericGrade2 + FunNumericGrade3 + FunNumericGrade4 + FunNumericGrade5 + FunNumericGrade6) / 6.0


    print("The numeric value for {1} is: {0:.1f}".format(FunNumericGrade1, courseName[0]))
    print("The numeric value for {1} is: {0:.1f}".format(FunNumericGrade2, courseName[1]))
    print("The numeric value for {1} is: {0:.1f}".format(FunNumericGrade3, courseName[2]))
    print("The numeric value for {1} is: {0:.1f}".format(FunNumericGrade4, courseName[3]))
    print("The numeric value for {1} is: {0:.1f}".format(FunNumericGrade5, courseName[4]))
    print("The numeric value for {1} is: {0:.1f}".format(FunNumericGrade6, courseName[5]))
  
    print("Your grade point average for the semester is: {0:.1}".format(averageGrade))

#FUNCTION
def fucCalculator(courseName):

    numericGrade = 0.0

    #Gather user inputs
    letterGrade = input("Please enter a letter grade for {0}: ".format(courseName)).upper()
    modifier = input("Please enter a modifier (+, - or nothing) : ")

    # Determine base numeric value of the grade
    if letterGrade == "A":
        numericGrade = 4.0
    elif letterGrade == "B":
        numericGrade = 3.0
    elif letterGrade == "C":
        numericGrade = 2.0
    elif letterGrade == "D":
        numericGrade = 1.0
    elif letterGrade == "F":
        numericGrade = 0.0
    else:
        #If an invalid entry is made
        print("You entered an invalid letter grade.")
    
    # Determine whether to apply a modifier
    if modifier == "+":
        if letterGrade != "A" and letterGrade != "F": # Plus is not valid on A or F
            numericGrade += 0.3
    elif modifier == "-":
        if letterGrade != "F":     # Minus is not valid on F
            numericGrade -= 0.3

    # Output final message and result, with formatting
    
    return numericGrade
#PROGRAM STARTS HERE
if __name__ == "__main__":
    main()