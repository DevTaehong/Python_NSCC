#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Taehong Min
Program Title:  Restaurant Bill
Description:    Tech check #1
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    #INPUT
    originalBill = input("Please enter your original bill amount: ")

    #PRECESSING
    valueOfTax = 0.15
    valueOfTip = 0.20
    tax = float(originalBill) * valueOfTax
    tip = float(originalBill) * valueOfTip
    totalOfBill = float(originalBill) + tax + tip 

    #OUTPUT
    print("Your original bill amount is: {0}".format(originalBill))
    print("Your tax is: {0:.2f}".format(tax))
    print("Your tip is: {0:.1f}".format(tip))
    print("Your total is: {0:.2f}".format(totalOfBill))

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()