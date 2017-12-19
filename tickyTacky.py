
#TIC TAC TOE GAME

import random


def main():
    tow = {"1" : '1', "2" : '2', "3" : '3',
    "4" : '4', "5" : '5', "6" : '6',
    "7" : '7', "8" : '8', "9" : '9'}
    player_choose = input("Select X or O: ")

    if player_choose.upper() == "X":

        while True:
            inception = ""
            player_turn(tow, 'X') #player X
            inception = win("X", tow)
            if inception == "return":
                return

            ai_turn(tow, 'O') #player O
            inception = win("O", tow)
            if inception == "return":
                return
    return


def ai_turn(tow, player):
    openPositions = []
    for value in tow.values(): #go through all values in dict list
        if value.isdigit() == True: #makes copy of tow dict
            openPositions.append(value)
            test_tow = dict(tow)
            test_tow[value] = player #run player_turn funct and try to use the for loop values
            ai_win = win(player, test_tow)
            if ai_win == player:
                tow[value] = player
    ai_decision = random.randint(0,len(openPositions)-1)
    tow[openPositions[ai_decision]] = player

def board_print(tow): #creates game board
    #creates top 3 place holders
    print(tow["1"] + ' | ' + tow["2"] + ' | ' + tow["3"])

    #creates mid 3 place holders
    print(tow["4"] + ' | ' + tow["5"] + ' | ' + tow["6"])

    #creates bottom 3 place holders
    print(tow["7"] + ' | ' + tow["8"] + ' | ' + tow["9"])
    print() #prints empty spaces
    return


def results(player): #shows which player won game
    print("Congrats! Player " + player + " you are the winner!!!")
    return "return"


def win(player, tow):
    inception = ""
    if tow["1"] == tow["2"] and tow["2"] == tow["3"]:
        inception = results(player)
        return

    if tow["4"] == tow["5"] and tow["5"] == tow["6"]:
        inception = results(player)

    if tow["7"] == tow["8"] and tow["8"] == tow["9"]:
        inception = results(player)

    if tow["1"] == tow["4"] and tow["4"] == tow["7"]:
        inception = results(player)

    if tow["2"] == tow["5"] and tow["5"] == tow["8"]:
        inception = results(player)

    if tow["3"] == tow["6"] and tow["6"] == tow["9"]:
        inception = results(player)

    if tow["1"] == tow["5"] and tow["5"] == tow["9"]:
        inception = results(player)

    if tow["3"] == tow["5"] and tow["5"] == tow["7"]:
        inception = results(player)


    counter = 0
    for value in tow.values():
        if value.isdigit() == False: #if letter, add 1 to counter
            counter += 1

    if counter == 9:
        board_print(tow)
        print("KATS!")
        return "return"


    if inception == "return":
        return "return"


def player_turn(tow, player):
    board_print(tow) #calling out the board_print funct
    var = input(player + " 's turn. Pick a number: ")
    while True:
        try:
            #input has to be a single integer and within range
            if int(var) in range(1,10) and len(var) == 1 and var != 0:
                #ensures a previous selection is not selected again
                if tow[var] == 'X' or tow[var] == 'O':
                    var = input('Position taken. Try again: ( ')
                else:
                    tow[var] = player #replaces number with x
                    break #breaks loop
        except:
            #notifies player if input is unexpected(not int or in range)
            var = input('Invalid character.')
    return

main()
