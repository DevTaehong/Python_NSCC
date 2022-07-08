#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Taehong Min    
Program Title:  The A-Team
Description:    A program that reads the text from a provided text file into a list, displays the text on-screen
"""
import random #Import random fuction
def alterInformation(numberOfLines ,lineToDelete, lines, outputFile): #four parameters
    for line in range(1, numberOfLines + 1): #starting range 1
        if line != lineToDelete: #using the "if" in order to omit a sentence
            if len(lines[line - 1]) <= 20: # when value less than 20 UPPER CASING
                print(str(line) + ": " + lines[line - 1].upper()) 
                outputFile.write(str(line) + ": " + lines[line - 1].upper() + "\n") #Writing to outputFile to make the new file
            else:
                print(str(line) + ": " + lines[line - 1].lower()) # When the value is greater than 20, LOWER CASING
                outputFile.write(str(line) + ": " + lines[line - 1].lower() + "\n")  
        else: #Omitting a sentence
            print() 
            outputFile.write("\n")

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    lines = [] #Initializing a list
    inputFile = open("ateam_Original.txt","r") #reading a file
    outputFile = open("ateam_Modified.txt","w") #writing a file

    print("---------------------------------------------")
    print("Original Text")
    print("---------------------------------------------")

    # Reading Input Text File into lines list
    for line in inputFile: #line by line
       line = line.rstrip("\n") #Remove the trailing characters if it is \n
       lines.append(line) #Appending valuable line to the lines list
       print(line)
    inputFile.close() #Closing the file
    
    # Alter information of ogiginal file
    print()
    print("---------------------------------------------")
    print("Altered Text")
    print("---------------------------------------------")
    numberOfLines = len(lines) #Setting a valuable of len(lines)
    lineToDelete = random.randint(1, numberOfLines) #Making random number starting 1
    alterInformation(numberOfLines, lineToDelete, lines, outputFile) #Setting a function
           
    outputFile.close() #Closing the file
                
    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()