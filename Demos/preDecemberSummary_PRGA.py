userHours = [8, 14, 6, 14, 7, 14, 14]

maxValue = max(userHours)

for day in range(len(userHours)):
    if userHours[day] == maxValue:
        print("Day # " + str(day + 1) + " was the max hours")

# print(maxValue)

# print("Hooked up to the list directly")
# for i in petList:
#     print(i)

# print("\nHooked up to range()")
# for i in range(len(petList)):
#     print(petList[i])