#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Taehong Min   
Program Title:  Weekly Loan Calculator
Description:    Developing a short term loan calculator program
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    #INPUT
    #Intro Message and input Messages 
    print("Weekly Loan Calculator\n")
    amountOfLoan = float(input("Enter the amount of loan: "))
    interestRate = float(input("Enter the interest rate (%): "))
    numberOfYears = float(input("Enter the number of years: "))

    #PROCESSING
    #Given Formula 
    i = interestRate / 5200

    #To calculate weekly payment Easily 
    fixedValue = float(1)
    
    #Given weekly payment Formula 
    weeklyPayment = (i / (fixedValue - (fixedValue + i) ** (-52 * numberOfYears))) * amountOfLoan
    
    #OUTPUT
    print("\nYour weekly payment will be: ${0:.2f}".format(weeklyPayment))

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()