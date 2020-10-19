#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Taehong Min 
Program Title:  Online Store
Description:    In class exercise!
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    print("Online Store")
    
    #User inputs - which country and order total
    orderAmount = float(input("Enter the amount of your order: $"))
    selectedCountry = input("What country are you from? ")

    #If the user is from Canada, ask which province
    if selectedCountry.lower() == "canada":
        province = input("Which province are you from? ")
        if province.lower() == "alberta":
            totalWithTax = orderAmount * 0.05
        elif province.lower() == "ontario" or province.lower() == "new brunswick" or province.lower() == "nova scotia":
            totalWithTax = orderAmount * 0.15
        else:
            totalWithTax = orderAmount * 0.11
        print("Your total with taxes for your order is ${0:.2f}".format(totalWithTax + orderAmount))
    
    #If the order is from outside Canada do not charge any taxes
    else:
        print("Your total order is {0:.2f}".format(orderAmount))

    

    #If the order was placed in Canada calculate tax based on the province
        #Alberta charge 5% GST
        
        #Ontario, NB, NS charge 15%

        #All other province charge 11%

    #Telling the user total with taxes for their order


    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()