#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name: Taehong Min   
Program Title:  Luggage Exercise
Description:    In class Exercise IF statements
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    print("Welcome to our airline")

    maxLimit = 50
    surchargeAmount = 25
    weight = input("Enter your luggage wieghts: ")

    if int(weight) > maxLimit:
        print("Your luggage exceeds the weight limit, a ${0} surcahge is applied.".format(surchargeAmount))

    if int(weight) <= maxLimit:
        print("Your luggahge is under the max weight limit, No surcahrge")

    print("Thank you for using our airline")

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()