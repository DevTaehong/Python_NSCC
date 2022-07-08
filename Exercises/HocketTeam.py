def main():

    #INPUT
    NameHockey = input("Please enter the name of a hockey team: ")
    
    #PROCESSING
    Wins = 10
    Losess = 5
    Percentage = Wins / (Wins + Losess)
    Ratio = 5
    Ratio1 = Wins / Ratio
    Ratio2 = Losess / Ratio

    #OUTPUT
    print("{0} have {1} wins and {2} losses, with a win percentage of {3:.4f} and win-loss ratio is {4:.0f} : {5:.0f} ".format(NameHockey, Wins, Losess, Percentage, Ratio1, Ratio2 ))



main()