# Expand on text adventure game, to include:
# - Add in functionality for diff creatures to fight

# - elif
# - and/or
# - Evaluating user inputs using logic

import random   #Import the random class, which contains random functionality, so I can use it in MY program

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
#goblinDmg = random.randint(1,10)
dragonDmg = random.randint(30,50)
flumphDmg = random.randint(75,100)
damageAmount = 0 #This is the var we'll use to hold diff damage amounts
chosenMob = ""  #Empty String

#User picks a monster
selectedMonster = input("Please select a monster:\nEnter 1 for goblin\nEnter 2 for dragon\nEnter 3 for flumph\nYour choice: ")

#Use the RANDOM.randint() function to let the PC randomly decide which monster to fight (Monster 1, 2 or 3)
selectedMonster = random.randint(1,3)

#Decision time! Decide between monster damage based on user choice
if selectedMonster.lower() == 1:    #Fighting the goblin
    print("Fighting the goblin")
    damageAmount = random.randint(1,10)
    chosenMob = "goblin"
elif selectedMonster == 2:  #Fighting the dragon
    print("Fighting the dragon")
    damageAmount = dragonDmg
    chosenMob = "dragon"
elif selectedMonster == 3:
    print("Fighting the flumph")
    damageAmount = flumphDmg
    chosenMob = "flumph"
# else:       #Else is optional, but frequently used, it's handy!
#      print("Whoops! You entered an incorrect choice!")

currentHP = boostedhp - damageAmount

# #Print new hp value to screen
#Include name of chosen monster in the hit msg
#Use the chosen monster's damage amount in the hit
print("You got hit by the " + chosenMob + " for " + str(damageAmount) + "! Your new hitpoints are ", currentHP)