def main():
    #INPUT - Number from user (# cups)
    print("Welcome to the Coffee shop!")
    print("This program will calculate total cost based on how many cups of coffee you order.")

    numberOfCups = input("Please enter the number of cups you wish to order: ")

    #PROCESSING - price * num of cups
    coffeePrice = 1.25
    Tax = 1.15
    TheCostBeforeTax = coffeePrice * int(numberOfCups)
    TheFinalCostIncludingTax = (coffeePrice * int(numberOfCups)) * Tax

    #OUTPUT - Message to user, indicating total cost
    print("The Cost before Tax: $", TheCostBeforeTax)
    print("The Final Cost including Tax: $", TheFinalCostIncludingTax)



main()
    