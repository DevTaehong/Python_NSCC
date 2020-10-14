#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Taehong Min 
Program Title:  Tax Withheld Calculator
Description:  Tech Check #2!!  
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    print("Tax Withholding Calculator")
    
    #INPUT
    weeklySalary = input("\nPlease enter the full amount of your weekly salary: ")
    dependents = input("How many dependents do you have?: ")

    #PROCESSING
    provinHoldingTax = 0.06
    federalHoldingTax = 0.25
    deduction = 0.02

    provinWhithheld = provinHoldingTax * float(weeklySalary)
    federalWhithheld = federalHoldingTax * float(weeklySalary)
    dependentDeduction = deduction * float(dependents) * float(weeklySalary)
    totalWithheld = provinWhithheld + federalWhithheld - float(dependentDeduction)
    totalTakehomepay = float(weeklySalary) - totalWithheld

    #OUTPUT
    print("\nProvincial Tax Withheld: ${0:.2f}".format(provinWhithheld))
    print("Federal Tax Withheld: ${0:.2f}".format(federalWhithheld))
    print("Dependent Deduction for {0} dependents: ${1:.2f}".format(dependents, dependentDeduction))
    print("Total Withheld: ${0:.2f}".format(totalWithheld))
    print("Total Take-Home Pay: ${0:.2f}".format(totalTakehomepay))


    



    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()