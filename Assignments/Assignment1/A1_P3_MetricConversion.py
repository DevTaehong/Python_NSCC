#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Taehong Min 
Program Title:  Imperial to Metric Conversion
Description:    xxxxxx
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    #INPUT
    print("Imperial To Metric Conversion\n")
    tons = int(input("Enter the number of tons: "))
    stone = int(input("Enter the number of stone: "))
    pounds = int(input("Enter the number of pounds: "))
    ounces = int(input("Enter the number of ounces: "))


    #PROCESSING
    
    totalOunces = 35840 * tons + 224 * stone + 16 * pounds + ounces #183716- 온스값으로 모두 환산된
    totalKilos = float(totalOunces) / 35.274
    metricTons = int(totalKilos / float(1000)) #미터법 톤은 5.208255372
    grams = 

    #OUTPUT
    print("\nThe metric weight is {0} metric tons, {1} kilos, and {2:.1f} grams.\n".format(metricTons, totalKilos, grams))
    


    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()