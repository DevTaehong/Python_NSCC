#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Geoff
Program Title:  String Manipulation Demo program
Description:    Program for exploring how to play with strings
"""

def main(): #<-- Don't change this line!
    #Welcome/intro message
    print("\nWelcome to the String Manipulator!")
    print("\nThis program will take a word or phrase you enter and TOTALLY AMAZE YOU WITH DIFF VERSIONS OF IT!!!\n")

    #Get a user-entered phrase (string)
    userEntry = input("Please enter a word or phrase to be manipulated: ")

    #Confirm phrase to user
    print("The phrase you entered is: {0}".format(userEntry))

    # STRING MANIUPLATIONS START HERE
    #Display phrase in all uppercase
    upperizedPhrase = userEntry.upper()
    print("Your phrase all in uppercase: {0}".format(upperizedPhrase))

    #Display phrase in all lowercase
    print("Your phrase all in lowercase: {0}".format(userEntry.lower()))

    #Display count of lowercase O's in phrase
    print("There are {0} lowercase O's in your phrase.".format(userEntry.count("o")))

    #Determine whether phrase is all alpha-numeric or not (T/F)
    print("Is this phrase alpha numeric? {0}".format(userEntry.isalnum()))

    #Change phrase to replace any lower S's to lower Z's    (replace())
    changerizedPhrase = userEntry.replace("s", "z")
    print("Your phrase with Z replacements: {0}".format(changerizedPhrase))


#Do not change any of the code below!
if __name__ == "__main__":
    main()