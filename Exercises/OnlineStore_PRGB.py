#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    
Program Title:  
Description:    
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    taxRate_AB = 0.05
    taxRate_ONNSNB = 0.15
    taxRate_Other = 0.11
    taxAmount = 0

    print("Online Store")

    #User inputs - Which country and order total
    orderAmount = float(input("Enter the amount of your order: $"))
    selectedCountry = input("What country are you from? ")

    #If Canada was the country, ALSO ask which province
    if selectedCountry.lower() == "canada": #ALWAYS REMEMBER THE PARENTHESIS AFTER A FUNCTION (it means run it)
        print("So you're Canadian, eh?")
        province = input("Which province/territory are you from?").lower()
        provTaxRate = 0
        if province == "alberta":   #If AB, 5%
            print("AB")
            provTaxRate = taxRate_AB
                #F                 or  T           or      T     =True      
        elif province == "ontario" or province =="nova scotia" or province =="new brunswick":#If NS, NB or ON, 15%
            print("ON/NS/NB")
            provTaxRate = taxRate_ONNSNB
        else:        #If any other prov/terr, 11% tax
            print("Other prov/terrs")
            provTaxRate = taxRate_Other

        #Calculate taxes
        taxAmount = orderAmount * provTaxRate

    else:
        print("You are NOT Canadian.")
        #IF not Canada, no taxes applied

    #Display totals with taxes, based on user's chosen country/prov values (if applicable)
    finalAmountOwed = orderAmount + taxAmount
    print("You owe us ${0:.2f}".format(finalAmountOwed))

    print("Thanks for shopping! Please come again!")

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()