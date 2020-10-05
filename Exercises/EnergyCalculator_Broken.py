"""
Student Name:  Taehong Min  
Program Title:  Energy Calculator - BROKEN
Description:   Debugging practice
"""

def main(): #<-- Don't change this line!
    
    print("Energy Calculator")
    print("\nThis program will calculate how much you pay for electricity for")
    print("a particular device, based on the wattage of the device and how")
    print("many hours the device was in use.")
    print("\nCalculations are based on a cost of 12.65 cents per kiloWatt hour.")

    kwhPrice = 12.65
    avgDaysInAMonth = 30.42
    monthsInYear = 12
    
    deviceWattage = float(input("\nEnter the wattage of the device: "))
    hoursUsedPerDay = float(input("Enter how many hours per day the device is in use: "))

    kwhPerDay = (deviceWattage /1000) * hoursUsedPerDay #BUG HERE <undefined-variable>
    costPerHour = (kwhPerDay * kwhPrice / 100) / 24 #BUG HERE <Wrong calulation, 
    costPerDay = kwhPerDay * kwhPrice / 100 # BUG HERE <Wrong calculation, it shold be = E(kWh/day) * kwhPrice / 100>
    costPerMonth = costPerDay * avgDaysInAMonth #BUG HERE < Wrong calculation>
    costPerYear = monthsInYear * costPerMonth #BUG HERE <Unused variable>
    

    print("\nElectrical cost for a device using {0:.2f} watts for {1} hour per day:".format(deviceWattage, hoursUsedPerDay)) #BUG HERE <Too many arguments for format string>
    print("\tCost Per Hour:\t${0:.5f}".format(costPerHour)) 
    print("\tCost Per Day:\t${0:.4f}".format(costPerDay))
    print("\tCost Per Month:\t${0:.3f}".format(costPerMonth))
    print("\tCost Per Year:\t${0:.2f}".format(costPerYear))
    print("\tkWh Per Day:\t{0:.1f}".format(kwhPerDay))

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()