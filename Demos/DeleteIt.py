#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    
Program Title:  
Description:    
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
   
    fileName = "names.txt"
    accessMode = "r"

    with open(fileName, accessMode) as myFile:
        # fileContentsString = myFile.read()
        # print(fileContentsString)
        # for i in range(4):
        #     if i == 3:
        #         lineContentString = myFile.readline()
        #         print(lineContentString)
        #     else:
        #         lineContentString = myFile.readline()
        #         print(lineContentString, end="")
        import csv
        fileContents = csv.reader(myFile)

        

    # try:
    #     myFile = open(fileName, accessMode)
    # except FileNotFoundError:
    #     print("An error occurred")
    # except:
    #     print("An error occurred")
    # finally:
    #     myFile.close()

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()
