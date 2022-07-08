#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    
Program Title:  
Description:    
"""
import csv

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    list = [] #Setting a list
    print("The Itsy Bitsy Aardvark")

    with open("the_choices_file.csv", "r") as choicesFile:
        csvFile = csv.reader(choicesFile)
        for i in csvFile:
            list.append(i) #Adding a list with the csv file

    user_choices = [] #Adding user word choices
    for row in list:
        print("\nPlease choose " + str(row[0]) + ":")
        for col in range(1, len(row)):
            print(str(col) + ") " + str(row[col]))
        while True:
            try:
                choice = int(input("Enter choice (1-5): "))
                if 1 <= choice <= 5:
                    user_choices.append(row[choice].upper())
                    break
            except ValueError:
                pass
    
    print("Your Completed Story:\n")
    with open("the_story_file.txt") as storyFile:
        for line in storyFile:
            tokens = line.strip().split(" ")
            for i in range(len(tokens)):
                token = tokens[i]
                if token[0] == token[-1] == "_":
                    n = int(token[1:-1])
                    tokens[i] = user_choices[n - 1]
            print(" ".join(tokens))

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()
