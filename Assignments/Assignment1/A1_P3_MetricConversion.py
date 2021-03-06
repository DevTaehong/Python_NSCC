#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Taehong Min 
Program Title:  Imperial to Metric Conversion
Description:    A conversion console program 
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    #INPUT
    #Intro Message and 3 input Message 
    print("Imperial To Metric Conversion\n")
    tons = int(input("Enter the number of tons: "))
    stone = int(input("Enter the number of stone: "))
    pounds = int(input("Enter the number of pounds: "))
    ounces = int(input("Enter the number of ounces: "))

    #PROCESSING
    # 3 required formulas
    totalOunces = 35840 * tons + 224 * stone + 16 * pounds + ounces 
    totalKilos = float(totalOunces) / 35.274 
    metricTons = int(totalKilos / float(1000)) 

    #To display left kilos of metric tons
    metricTonsFloat = totalKilos / float(1000)

    #left values of metric tons
    leftKilos = (metricTonsFloat - metricTons) * 1000
    grams = (totalKilos - int(totalKilos)) * 1000

    #OUTPUT
    print("\nThe metric weight is {0} metric tons, {1} kilos, and {2:.1f} grams.\n".format(metricTons, int(leftKilos) , grams))
    
    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()