# Taxed Coffee Shop program
# Simple program to demonstrate math calcs, use of 
#variables, datatypes, operators again
#Also, Datatype casting

#Two outputs - Total before and after tax

#How do we get input from the user through console?
#How to concatenate!
#Rounding, working with diff datatypes      round(,)

priceOfCoffee = 1.55    #<-- Business sets these (not cust)
numOfCups = 1           #<-- Value user entered
taxRate = 1.15          #<-- Business sets these (not cust)

#Welcome message(s) and user prompts/info
print("Welcome to my Coffee Shop!")
print("We sell premium coffee for $" + str(priceOfCoffee) + " per cup! It's awesome!")

#Get num of cups from the user
numOfCups = input("How many cups would you like? ") #INPUT ALWAYS GIVES YOU A STRING.

# int("123")  --> 123
# str(456)    --> "456"
# float()

#Do some calculations (math) price X quantity
#Step 1 of math calcs (total before tax)
preTaxTotal = priceOfCoffee * int(numOfCups)

#Step 2 - Total incl. tax (multiply pretaxtotal by 1.15 (15%))
postTaxTotal = preTaxTotal * taxRate

#Rounding
roundedPreTax = round(preTaxTotal, 2)
roundedPostTax = round(postTaxTotal, 2)

#Output to screen
print("Your pre-tax total is $" + str(roundedPreTax))
print("Your total including tax is $" + str(roundedPostTax))

#Concatenation - Adding multiple strings together (end to end)
# 2+3 --> 5
# "snow" + "ball" --> "snowball"
# "2" + "3" --> "23"