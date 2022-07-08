#2d lists

# def shuffleList(prm_number, prm_two, prm_three):
    
#     returnList = []
#     x = 1
#     y = 2
#     z =3
#     returnList.append(x)
#     returnList.append(y)
#     returnList.append(z)

#     return returnList

#               0       1       2
twoDlist = [[1,2,3], [4,5,6], [7,8,9]]

result = 0
for row in range(len(twoDlist)):
    for col in range(len(twoDlist)):
        if col == 1:
            result += twoDlist[row][col]

print(result)
#row  col
# 0   0
# 0   1
# 0   2
# 1   0
# 1   1
# 1   2
# 2   0  
# 2   1
# 2   2

# print(twoDlist[2][1])

# num = 12
# someList = shuffleList(num, "hi", "banana")

# someList.append(7)
# someList.sort()
# someList.reverse()

# for value in someList:
# #     print(value)

# name = input("Enter your name: ")
# if name in ("Geoff", "Dustin"):
#     print("HI GUYS!")
# else:
#     print("Nope")