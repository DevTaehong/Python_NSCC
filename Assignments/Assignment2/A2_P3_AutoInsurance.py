#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Taehong Min
Program Title:  Auto Insurance
Description:    Writing a program that computes monthly insurance
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #Variables and Initializing 
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
    #Input message!!
    gender = input("Are you 'Male' or 'Female': ").lower() #for lower case
    age = int(input("Enter your age: "))
    price = float(input("Enter the purchase price of the vehicle: "))
    
    #PROCESSING
    #Decision between Male and Female
    #If male
    if gender == "male":
        # If age is 15 or greater but less than 25, 25% of price
        if age >= fistAge and age < secondAge:
            monthlyPrice =  price * firstMalePriceRate / monthOfYear
        # If age is 25 or greater but less than 40, 17% of pirce
        elif age >= secondAge and age < thirdAge:
            monthlyPrice =  price * secondMalePriceRate / monthOfYear
        # If age is 40 or greater but less than 70, 10% of price
        elif age >= thirdAge and age < lastAge:
            monthlyPrice =  price * lastMalePriceRate / monthOfYear

    #If female
    elif gender == "female":
        # If age is 15 or greater but less than 25, 20% of price
        if age >= fistAge and age < secondAge:
            monthlyPrice =  price * firstFemalePriceRaTe / monthOfYear
        # If age is 25 or greater but less than 40, 15% of price
        elif age >= secondAge and age < thirdAge:
            monthlyPrice =  price * secondFemalePriceRaTe / monthOfYear
        # If age is 40 or greater but less than 70, 10% of price
        elif age >= thirdAge and age < lastAge:
            monthlyPrice =  price * lastFemalePriceRaTe / monthOfYear

    #OUTPUT
    print("Your monthly insurance will be ${0:.2f}".format(monthlyPrice))

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()