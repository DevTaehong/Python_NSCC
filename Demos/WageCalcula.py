#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Taehong Min
Program Title:  Wage Calculrate
Description:    In calss exercise
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #Welcome content
    print("Wage Calculator")

    #INPUT
    hoursWork = float(input("Enter the number of hours you worked this week: "))
    dollarPerHour = float(input("Enter the dollar amount you make per hour: $"))
    
    #PROCESSING
    exceeds = 40
    otRate = 1.5
    otPay = 0.0
    
    if hoursWork > exceeds:
        otHours = hoursWork - exceeds
        otPay = otHours * (dollarPerHour * otRate)
        regPay = dollarPerHour * exceeds

    else:
        regPay = hoursWork * dollarPerHour

    totalPay = otPay + regPay
    #OUTPUT
    print("Your total wage is: ${0:.2f}".format(totalPay))

    
    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()