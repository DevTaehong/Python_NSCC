#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    
Program Title:  
Description:    
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #Name of the file?
    #Location of the file?
    #(type of file)
    #Purpose of use?
    fileName = "Files\pets.csv"  #Default location is the root of your workspace folder
    accessMode = "w"        # "w" write to file     "a" append data       "r" read data from file

    petList = [["Puppy", "Buster", "4"],
                ["Kitty", "Fluffy", "2"],
                ["Fish", "Swimmy", "12"]]

    #Gathering pet names from the user and adding them to list
    # while True:
    #     name = input("What pet type do you want to add? (done to quit) ")
    #     if name.lower() == "done":
    #         break
    #     petList.append(name)

    myFile = open(fileName, accessMode)

    #2d list example, writing to file
    for row in range(len(petList)):     #Loop for going row by row
        for col in range(len(petList[row])):
            myFile.write(petList[row][col])
            if col != 2:    #I'm at the end of the cols in this row
                myFile.write(",")
            else:
                myFile.write("\n")

    #Loop through the list and write each pet name to file
    # for i in range(5):           0 1 2 3 4
    #     if petList[i] == "Mongoose":
    #         myFile.write("AHHHHHHHH\n")
    #     else:
    #         myFile.write(petList[i] + "\n")

    # for oompaloompa in petList:
    #     myFile.write(oompaloompa)


    # myFile.write("Dog\n")           #YOU have to add your own line breaks
    # myFile.write("Cat\n")           #ALSO .write() ONLY accepts strings
    # myFile.write("Fish\n")

    myFile.close()  #ALWAYS REMEMBER TO CLOSE YOUR FILE CONNECTIONS

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()