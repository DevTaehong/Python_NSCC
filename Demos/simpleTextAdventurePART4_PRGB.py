# Expand on text adventure game, to include:
# - Add in functionality for diff creatures to fight

# - elif
# - and/or
# - Evaluating user inputs using logic

import random   #Import the random class, which contains random functionality, so I can use it in MY program

def doTheFight(currentCreatureName, lowerRange, upperRange):
    #Print a fight msg
    #Set damage amount
    #Set creature name

    print("IT's ON!!!!!!")
    print("You're fighting the " + currentCreatureName + "!!! GOOD LUCK!")
    damageAmount = random.randint(lowerRange, upperRange)
    return damageAmount


originalHP = 250

hpBoostAmount = 10

#Set the stage (welcome/contextual message)
print()
print("Welcome to python quest, a text adventure to test new thingys that get learned.")
print("This is a text adventure game, have fun!")
print()

#User can enter the name of their character
characterName = input("Please enter your character's name: ")

#Three different ways to concatenate values together to get one big sentence
#print("You are a warrior named " + characterName + " and your starting hitpoints are " + str(originalHP))     #Manual
#print("You are a warrior named", characterName ,"and your starting hitpoints are", str(originalHP))    #print() with multiple values
print("You are a warrior named {0} and your starting hitpoints are {1:.0f}".format(characterName, originalHP))  #string.format()

#Do the potion hp boost
boostedhp = originalHP + hpBoostAmount
print("You drink a mysterious potion. You get {0} more hitpoints! You now have {1}".format(hpBoostAmount, boostedhp))

# Do some math! (Subtract damage amount from original hp)
# Result: New hit point amount (current health)
# Let's FIGHT!
#Allow user to choose which creature to fight (select a number when prompted)
selectedMonster = 0
damageAmount = 0 #This is the var we'll use to hold diff damage amounts
chosenMob = ""  #Empty String

#Use the RANDOM.randint() function to let the PC randomly decide which monster to fight (Monster 1, 2 or 3)
selectedMonster = random.randint(1,4)

#Decision time! Decide between monster damage based on user choice
if selectedMonster == 1:    #Fighting the goblin
    chosenMob = "goblin" 
    damageAmount = doTheFight(chosenMob, 1, 10)

elif selectedMonster == 2:  #Fighting the dragon
    chosenMob = "dragon" 
    damageAmount = doTheFight(chosenMob, 40, 50)

elif selectedMonster == 3:
    chosenMob = "flumph" 
    damageAmount = doTheFight(chosenMob, 75, 100)

elif selectedMonster == 4:
    chosenMob = "beholder" 
    damageAmount = doTheFight(chosenMob, 275, 362)

currentHP = boostedhp - damageAmount

# #Print new hp value to screen
#Include name of chosen monster in the hit msg
#Use the chosen monster's damage amount in the hit
print("You got hit by the " + chosenMob + " for " + str(damageAmount) + "! Your new hitpoints are", currentHP)

if currentHP < 0:
    print("YOU DIED! GAME OVER")