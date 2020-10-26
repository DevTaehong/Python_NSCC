#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Taehong Min
Program Title:  Auto Insurance
Description:    Writing a program that computes monthly insurance
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    fistAge = 15
    secondAge = 25
    thirdAge = 40
    lastAge = 70
    monthlyPrice = 0.0
    monthOfYear = 12
    firstMalePriceRate = 0.25
    secondMalePriceRate = 0.17
    lastMalePriceRate = 0.10
    firstFemalePriceRaTe = 0.20
    secondFemalePriceRaTe = 0.15
    lastFemalePriceRaTe = 0.10
    
    #INPUT
    gender = input("Are you 'Male' or 'Female': ").lower()
    age = int(input("Enter your age: "))
    price = float(input("Enter the purchase price of the vehicle: "))
    
    #PROCESSING
    if gender == "male":
        if age >= fistAge and age < secondAge:
            monthlyPrice =  price * firstMalePriceRate / monthOfYear
        elif age >= secondAge and age < thirdAge:
            monthlyPrice =  price * secondMalePriceRate / monthOfYear
        elif age >= thirdAge and age < lastAge:
            monthlyPrice =  price * lastMalePriceRate / monthOfYear

    elif gender == "female":
        if age >= fistAge and age < secondAge:
            monthlyPrice =  price * firstFemalePriceRaTe / monthOfYear
        elif age >= secondAge and age < thirdAge:
            monthlyPrice =  price * secondFemalePriceRaTe / monthOfYear
        elif age >= thirdAge and age < lastAge:
            monthlyPrice =  price * lastFemalePriceRaTe / monthOfYear

    #OUTPUT
    print("Your monthly insurance will be ${0:.2f}".format(monthlyPrice))

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()