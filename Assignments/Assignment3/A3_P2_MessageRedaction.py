#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Taehong Min
Program Title:   Message Redaction
Description:     A program that removes all desired letters from any user-entered sentence or phrase.
"""
#Settig a fuction and to print Redacted Phrases
def redactedPhrase(phrase, redactletters): 
    for i in phrase: #Looping User input phrase and seperate to letters
        for x in redactletters: #User input letters to redact and seperate it to a letter
            if i == x:
                printRemovedLetters = phrase.replace(x, "_") #Replacing redact letters to "_"
    for i in printRemovedLetters: #To replace redact letter, looping it again
        for x in redactletters:
            if i == x:
                printRemovedLetters2 =  printRemovedLetters.replace(x, "_")
                if len(redactletters) <= 5:
                    return printRemovedLetters2 #Returning it to print
    if len(redactletters) > 5: # Only letters to redact are over 5
        for i in printRemovedLetters2:
            for x in redactletters:
                if i == x:
                    printRemovedLetters3 = printRemovedLetters2.replace(x, "_")
                    return printRemovedLetters3
        
def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #Initializing Valuables
    numberOfLetters = 0
    message = []
    phrase = ""
    redactletters = []


    while phrase != "QUIT": #When user put quit, program ends
        phrase = input("\nType a phrase (or quit to exit program): ").upper()
        for x in phrase:
            message.append(x)
        if phrase != "QUIT":
            redact = input("\nType a comma-separated list of letters to redact: ").upper()
            for seperateRedact in redact:
                redactletters.append(seperateRedact)
                for letter in phrase:
                    if letter == seperateRedact:
                        numberOfLetters += 1 #Counting letter removed
            print("Number of letters redacated: {0}".format(numberOfLetters))
            numberOfLetters = 0 #Initializing again
            finalPhrase = redactedPhrase(phrase, redactletters) #Return value setting
            print(finalPhrase.lower()) 
            redactletters = [] #Initializing again
                


    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()