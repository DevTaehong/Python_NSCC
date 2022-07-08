#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Taehong Min
Program Title:  Girl Guide Cookie Sell-off
Description:    A program to print the guide list and their prizes.
"""
#Settig a fuction
def average(numberBoxesList):
    totalAverage = 0.0 #Initializing
    for x in range(len(numberBoxesList)): #Setting range by using numberBoxesList's length
        Averages = numberBoxesList[x] / len(numberBoxesList)
        totalAverage += Averages #Whenever looping plus averages variable
    return totalAverage #Return this value

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #Initializing
    numberGuides = int(input("Enter the number of guides selling cookies: "))
    nameGuideList = []
    numberBoxesList = [] 

    for x in range(numberGuides): #Range set numberGuides variable's value
        nameGuide = (input("\nEnter the name of guide #{0}: ".format(x + 1)))
        numberBoxes = (int(input("Enter the number of boxes sold by {0}: ".format(nameGuide))))
        nameGuideList.append(nameGuide) #Adding to the list named nameGuideList
        numberBoxesList.append(numberBoxes) #Adding to the list named numberBoxesList
    
    totalAverage = average(numberBoxesList) #Return value set to this variable
    
    print("\n\nThe average number of boxes sold by by each guide was {0:.1f}".format(totalAverage))
    print("\nGuide       Prizes Won:\n------------------------------------------------")
                  
    for n in range(numberGuides): #Range set numberGuides's value     
        if max(numberBoxesList) == numberBoxesList[n]: #Check if the highest selling guide
            print("{:<10} - Trip to Girl Guide Jamboree in Aruba!".format(nameGuideList[n]))

        elif totalAverage < numberBoxesList[n]: #Check if a guide sold above average
            print("{:<10} - Super seller Badge".format(nameGuideList[n]))
                                          
        elif numberBoxesList[n] >= 1 and numberBoxesList[n] < totalAverage: #Check if a guide sold at least one box
            print("{:<10} - Left over cookies".format(nameGuideList[n]))

        elif numberBoxesList[n] == 0: #Check if a guide sold nothing
            print("{:<10} - ".format(nameGuideList[n]))
        

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()