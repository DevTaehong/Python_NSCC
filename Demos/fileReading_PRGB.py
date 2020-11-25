#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    
Program Title:  
Description:    
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #Connect to my file
    fileName = "Files/pets.csv"
    accessMode = "r"        #Read mode

    # try:
    with open(fileName, accessMode) as myFile:
        #Example of using .read()   (Entire contents as a string)
        #fileContentsString = myFile.read()
        # print(myFile.read())   #includes "special" chars like line breaks

        #Example 2 - .readline()     *Reads contents one line at a time as a string
        # lines = []
        # for i in range(4):
            # lineContentString = myFile.readline()   #Works off the line breaks
            # if i == 2:
            #     print(lineContentString.upper(), end="")
            # else:
            #     print(lineContentString, end="")
        #     lineContentString = myFile.readline()
        #     lines.append(lineContentString)   #Example of putting each line into a list we created

        # lines.sort()
        # print(lines)

        # lines = myFile.readlines()      #Reads contents of file, returns as a list (based on line breaks)
        
        # for i in range(len(lines)):
        #     print(lines[i])

        #SOMETHING TO RESEARCH  .split()   .join()  THese change from string to list or vice versa

        #PART TWO - Reading CSV files
        import csv
        fileContents = csv.reader(myFile)   #Gives me something LIKE a 2d list containing the data in the file

        my2dList = []
        for row in fileContents:    #Loop through the fileContents NOT-QUITE-LIST
            my2dList.append(row)    #I could create my own 2d list out of the csv reader object
            # for col in row:
            #     print(col)

        print(my2dList)
    # except FileNotFoundError:
    #     print("The file specified for the program was not found.")
    # except:
    #     print("An error occurred")
    # finally:
    #     myFile.close()

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()