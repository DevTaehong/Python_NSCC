#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Taehong Min    
Program Title:  The Itsy Bitsy Aardvark
Description:    A program that presents the user with a “Mad Libs” type game
"""

import csv #import csv fuction

def makingStory(user_choices):
    with open("the_story_file.txt") as storyFile:
        for line in storyFile: #Looping the txt file line by line
            tokens = line.strip().split(" ") #Split the string into tokens which is a list
            for i in range(len(tokens)): 
                token = tokens[i] #Making the token variable, to check if it is a number string "_1_, _2_..."
                if token[0] == token[-1] == "_":
                    n = int(token[1:-1]) #Slicing strings starting index 1 to -1 index (But not included)
                    tokens[i] = user_choices[n - 1] #Replacing the list which is tokens with user_choices
            print(" ".join(tokens)) #Join all items


def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    list = [] #Initializing a list 
    print("The Itsy Bitsy Aardvark")

    with open("the_choices_file.csv", "r") as choicesFile: #Open the_choices_file.csv to read as ChoicesFile
        csvFile = csv.reader(choicesFile) #Reading a csv file
        for i in csvFile: #
            list.append(i) #Addending csvFile line by line to a list

    user_choices = [] #Adding user word choices
    for row in list: 
        print("\nPlease choose " + str(row[0]) + ":")
        for col in range(1, len(row)): #Starting index 1 in the list
            print(str(col) + ") " + str(row[col]))
        while True: #Setting infinite loop 
            try:
                choice = int(input("Enter choice (1-5): "))
                if 1 <= choice <= 5: # When a user selects number range 1-5, keep executing 
                    user_choices.append(row[choice].upper()) #Appending user's choices with upper case to the list
                    break #Keeping looping to next
            except ValueError:#When a user selects wrong number, passing
                pass
    
    print("Your Completed Story:\n")
    makingStory(user_choices)
    

    #Your code ends on the line above
#Do not change any of the code below!

if __name__ == "__main__":
    main()