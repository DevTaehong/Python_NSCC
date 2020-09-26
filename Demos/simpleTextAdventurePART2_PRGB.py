# Expand on text adventure game, to include:
# - User inputs the character name
# - User drinks a potion, gets extra hp prior to the fight
# - Output message to tell of hp boost
# - Do the fight with the goblin
# - Change our print statement to include more info (old hp, damage, new hp, character name)

# - Using the input() command
# - More calcs (math)
# - Explore diff ways of combining strings and values (string.format())

originalHP = 250
damageAmount = 20
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
print("You are a warrior named {0} and your starting hitpoints are {1:.6f}".format(characterName, originalHP))  #string.format()

#Do the potion hp boost
boostedhp = originalHP + hpBoostAmount
print("You drink a mysterious potion. You get {0} more hitpoints! You now have {1}".format(hpBoostAmount, boostedhp))

#Do some math! (Subtract damage amount from original hp)
# Result: New hit point amount (current health)
currentHP = boostedhp - damageAmount

# #Print new hp value to screen
print("You got hit for " + str(damageAmount) + "! Your new hitpoints are ", currentHP)