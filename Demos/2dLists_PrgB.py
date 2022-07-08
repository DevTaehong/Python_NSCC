#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    
Program Title:  
Description:    
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    x = 5
            #       0     1     2  
    geoffList = ["Geoff", 6, "blue"]    #1d list   (line)


    # for i in range(len(geoffList)):
    #     print(geoffList[i])

    my2dList = []
    my2dList.append(["Geoff", 6, "blue"])
    my2dList.append(["Ben", 6.11, "violet"])
    my2dList.append(["Colby", 6.7, "green"])

    #2d list  (square)
    names = [["Geoff", 6, "blue"],      # 0
            ["Matt", 5.10, "brown"],    # 1
            ["Cass", 5.8, "blue"],    # 2
            ["Colby", 6.7, "green"],    # 3
            ["Ben", 6.11, "Violet"]]    # 4

    for row in range(len(names)):         #i loop goes row by row
        for col in range(len(names[row])):  #j loop goes col by col IN the current i row
            print(names[row][col])

    # print(names[3][1])

    # nums = [[10, 20, 30, 40, 50],
    #         [100, 200, 300, 400, 500],
    #         [1000, 2000, 3000, 4000, 5000]    ]

    # print(nums)

    # nums[2][3] = input("Enter a number: ")

    # print(nums)

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()