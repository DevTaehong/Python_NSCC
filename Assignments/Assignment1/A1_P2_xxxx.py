#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name: Taehong Min   
Program Title:  Weekly Loan Calculator
Description:    xxxxxxxxxxx
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    #INPUT
    print("Weekly Loan Calculator\n")
    amountOfLoan = float(input("Enter the amount of loan: "))
    interestRate = float(input("Enter the interest rate (%): "))
    numberOfYears = float(input("Enter the number of years: "))
    


    #PROCESSING
    i = interestRate / 5200
    fixedvalue = float(1)

    weeklyPayment = (i / (fixedvalue - (fixedvalue + i) ** (-52 * numberOfYears))) * amountOfLoan
    
    #OUTPUT
    print("\nYour weekly payment will be: ${0:.2f}".format(weeklyPayment))
    




    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()