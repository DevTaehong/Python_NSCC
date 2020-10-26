#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Taehong Min
Program Title:  Erewhon Mobile Data Plans
Description:    A program will figure out which single range the usage falls into, then calculate
                the cost
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    dataPlan200 = float(200)
    dataPlan500 = float(500)
    dataPlan1000 = float(1000)
    rateCharge = 0.0
    #INPUT
    dataUsage = float(input("Enter data usage (Mb): "))

    #PROCESSING
    if dataUsage <= dataPlan200:
        rateCharge = 20.00

    elif dataUsage > dataPlan200 and dataUsage <= dataPlan500:
        rateCharge = 0.105 * dataUsage

    elif dataUsage > dataPlan500 and dataUsage <= dataPlan1000:
        rateCharge = 0.110 * dataUsage

    elif dataUsage > dataPlan1000:
        rateCharge = 118.00
        
    totalCharge = rateCharge 

    #OUTPUT
    print("\nTotal charge is ${0:.2f}".format(totalCharge))


    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()