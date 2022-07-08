#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Taehong Min 
Program Title:  Time sheet
Description:    A program that accepts the number of hours worked on each of five work days from the user
"""
#Settig a fuction and to print the total number of hours worked
def totalHours(first, second, thrid, forth, fifth): #setting 4 parameters
    inSideTotal = int(first) + int(second) + int(thrid) + int(forth) + int(fifth)
    return inSideTotal # return the value

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #Initializeing Variables 
    hoursWorked = []
    lessWorkHours = 7

    for days in range(1, 6): # Starting value 1 and goes until it hits 6
        hoursWorked.append(int(input("Enter hours worked on Day #{0}: ".format(days)))) #Adding to the list named hoursWorked
    print("--------------------------------------------------------------------")


    for i in range(5): # 0~4 range
        if max(hoursWorked) == int(hoursWorked[i]): #To find the most hours worked day
            print("The most hours worked was on:")
            print("Day #" + str(i + 1), "when you worked", max(hoursWorked), "hours.")

    #Setting a function
    finalTotalHours = totalHours(hoursWorked[0], hoursWorked[1], hoursWorked[2], hoursWorked[3], hoursWorked[4])
    print("--------------------------------------------------------------------")
    print("The total number of hours worked was: {0}".format(finalTotalHours))
    print("The average number of hours worked each day was: {0}".format(finalTotalHours / len(hoursWorked)))
    print("--------------------------------------------------------------------")
    print("Days you slacked off (i.e. worked less than 7 hours):")
    
    for x in range(5): #0~4 range
        if hoursWorked[x] < lessWorkHours: # If less than 7hours, it prints
            print("Day #" + str(x + 1) + ":", str(hoursWorked[x]), "hours")

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()