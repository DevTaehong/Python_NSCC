#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    
Program Title:  
Description:    
"""
import random

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #Program randomly picks a number
    #Ask user to pick a number between 1 and 100
    #Our program tells them higher or lower until they get it
    #Keep a count of how many guesses it took

    secretNumber = random.randint(1,100)    #Pick a secret number

    print("The Number Guessing Game\n")

    guessCount = 0

    while True:
        userGuess = input("Enter a number between 1 and 100: ")
        guessCount += 1
        # if userGuess.isnumeric():
        try:
            if userGuess == "200":  #Silly code put in just to invoke a zero division error
                5 / 0
            elif int(userGuess) < 1 or int(userGuess) > 100:
                print("Please enter a number in the range (1-100).")
            else:
                if int(userGuess) == secretNumber:
                    print("You win! You guessed that {} was the secret number!".format(secretNumber))
                    break
                elif int(userGuess) < secretNumber:
                    print("Wrong! The secret number is higher than that.")
                elif int(userGuess) > secretNumber:
                    print("Wrong! The secret number is lower than that.")
        except TypeError:   #This will run if an error with classification TypeError occurs
            print("We experienced a datatype problem")
        except ValueError:  #This will run if an error with classification ValueError occurs
            print("We experienced an expected value problem. (User probably entered a non-integer value).")
        except ZeroDivisionError:   #Ditto for a divide by zero error occurred
            print("You tried to divide by zero. AHHHHHHHHH (world implodes)")
            guessCount += 200
        except FileNotFoundError:
            print("That file doesn't exist.")
        except:     #This will run when an error occurs, if it isn't
                    #any of the exception types listed above
            print("Some OTHER UNEXPECTED error occurred.")

    print("You made {0} number of guesses to get the number.".format(guessCount))
    print("Game over!")

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()