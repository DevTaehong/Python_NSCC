#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Taehong Min    
Program Title:  Hipster's Local Vinyl Records
Description:    xxxxxxxxxx
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    #INPUT
    print("\nHipster's Local Vinyl Records - Customer Order Details")
    customerName = input("\nEnter the customer's name: ")
    numberKiloDistance = input("Enter the distance in kilometers for delivery: ")
    costOfAnyRecord = input("Enter the cost of records purchased: ")
    deliveryRate = 15
    saliesTax = 0.14

    #PROCESSING
    deliveryCost = (float(numberKiloDistance)) * float(deliveryRate)
    purchaseCost = float(costOfAnyRecord) * float(saliesTax) + float(costOfAnyRecord)
    totalCost = deliveryCost + purchaseCost

    #OUTPUT
    print("\nPurchase summary for {0} ".format(customerName))
    print("Delivery Cost: ${0:.2f}".format(deliveryCost))
    print("Purchase Cost: ${0:.2f}".format(purchaseCost))
    print("Total Cost   : ${0:.2f} \n".format(totalCost))


    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()