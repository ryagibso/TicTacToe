import os

def main():
    global cell_1
    global cell_2
    global cell_3
    global cell_4
    global cell_5
    global cell_6
    global cell_7
    global cell_8
    global cell_9
    global player
    global gameFinished
    global Xwins
    global Owins
    
    cell_1 = " "
    cell_2 = " "
    cell_3 = " "
    cell_4 = " "
    cell_5 = " "
    cell_6 = " "
    cell_7 = " "
    cell_8 = " "
    cell_9 = " "
    player = "X"
    gameFinished = False
    Xwins = 0
    Owins = 0

    #os.system("cls")
    print "#############"
    print "# 1 # 2 # 3 #"
    print "#############"
    print "# 4 # 5 # 6 #"
    print "#############"
    print "# 7 # 8 # 9 #"
    print "#############"

    playerMove()

def printBoard():
    global cell_1
    global cell_2
    global cell_3
    global cell_4
    global cell_5
    global cell_6
    global cell_7
    global cell_8
    global cell_9
    
    print "#############"
    print "# " + cell_1 + " # " + cell_2 + " # " + cell_3 + " #"
    print "#############"
    print "# " + cell_4 + " # " + cell_5 + " # " + cell_6 + " #"
    print "#############"
    print "# " + cell_7 + " # " + cell_8 + " # " + cell_9 + " #"
    print "#############"

def changePlayer():
    global player

    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"
    else:
        print "Player error"

def winCheck():
    global cell_1
    global cell_2
    global cell_3
    global cell_4
    global cell_5
    global cell_6
    global cell_7
    global cell_8
    global cell_9
    global gameFinished
    global Xwins
    global Owins

    if cell_1 == "X" and cell_2 == "X" and cell_3 == "X":
        print "Player X wins!"
        Xwins += 1
        print "X wins: " + str(Xwins)
        print "O wins: " + str(Owins)
        gameFinished = True
    if cell_4 == "X" and cell_5 == "X" and cell_6 == "X":
        print "Player X wins!"
        Xwins += 1
        print "X wins: " + str(Xwins)
        print "O wins: " + str(Owins)
        gameFinished = True
    if cell_7 == "X" and cell_8 == "X" and cell_9 == "X":
        print "Player X wins!"
        Xwins += 1
        print "X wins: " + str(Xwins)
        print "O wins: " + str(Owins)
        gameFinished = True

    if cell_1 == "X" and cell_4 == "X" and cell_7 == "X":
        print "Player X wins!"
        Xwins += 1
        print "X wins: " + str(Xwins)
        print "O wins: " + str(Owins)
        gameFinished = True
    if cell_2 == "X" and cell_5 == "X" and cell_8 == "X":
        print "Player X wins!"
        Xwins += 1
        print "X wins: " + str(Xwins)
        print "O wins: " + str(Owins)
        gameFinished = True
    if cell_3 == "X" and cell_6 == "X" and cell_9 == "X":
        print "Player X wins!"
        Xwins += 1
        print "X wins: " + str(Xwins)
        print "O wins: " + str(Owins)
        gameFinished = True

    if cell_1 == "X" and cell_5 == "X" and cell_9 == "X":
        print "Player X wins!"
        Xwins += 1
        print "X wins: " + str(Xwins)
        print "O wins: " + str(Owins)
        gameFinished = True
    if cell_3 == "X" and cell_5 == "X" and cell_7 == "X":
        print "Player X wins!"
        Xwins += 1
        print "X wins: " + str(Xwins)
        print "O wins: " + str(Owins)
        gameFinished = True



    if cell_1 == "O" and cell_2 == "O" and cell_3 == "O":
        print "Player O wins!"
        Owins += 1
        print "X wins: " + str(Xwins)
        print "O wins: " + str(Owins)
        gameFinished = True
    if cell_4 == "O" and cell_5 == "O" and cell_6 == "O":
        print "Player O wins!"
        Owins += 1
        print "X wins: " + str(Xwins)
        print "O wins: " + str(Owins)
        gameFinished = True
    if cell_7 == "O" and cell_8 == "O" and cell_9 == "O":
        print "Player O wins!"
        Owins += 1
        print "X wins: " + str(Xwins)
        print "O wins: " + str(Owins)
        gameFinished = True

    if cell_1 == "O" and cell_4 == "O" and cell_7 == "O":
        print "Player O wins!"
        Owins += 1
        print "X wins: " + str(Xwins)
        print "O wins: " + str(Owins)
        gameFinished = True
    if cell_2 == "O" and cell_5 == "O" and cell_8 == "O":
        print "Player O wins!"
        Owins += 1
        print "X wins: " + str(Xwins)
        print "O wins: " + str(Owins)
        gameFinished = True
    if cell_3 == "O" and cell_6 == "O" and cell_9 == "O":
        print "Player O wins!"
        Owins += 1
        print "X wins: " + str(Xwins)
        print "O wins: " + str(Owins)
        gameFinished = True

    if cell_1 == "O" and cell_5 == "O" and cell_9 == "O":
        print "Player O wins!"
        Owins += 1
        print "X wins: " + str(Xwins)
        print "O wins: " + str(Owins)
        gameFinished = True
    if cell_3 == "O" and cell_5 == "O" and cell_7 == "O":
        print "Player O wins!"
        Owins += 1
        print "X wins: " + str(Xwins)
        print "O wins: " + str(Owins)
        gameFinished = True

    if cell_1 != " " and cell_2 != " " and cell_3 != " " and cell_4 != " " and cell_5 != " " and cell_6 != " " and cell_7 != " " and cell_8 != " " and cell_9 != " ":
        print "It's a cat's game!"
        gameFinished = True
    
def playerMove():
    global cell_1
    global cell_2
    global cell_3
    global cell_4
    global cell_5
    global cell_6
    global cell_7
    global cell_8
    global cell_9
    global player
    global gameFinished

    playAgain = True
    choice = ""
    
    while playAgain == True:
        while gameFinished == False:
            cell = input("Enter the number of an empty cell to enter " + player + " in: ")
            
            if cell == 1:
                if cell_1 == " ":
                    cell_1 = player
            elif cell == 2:
                if cell_2 == " ":
                    cell_2 = player
            elif cell == 3:
                if cell_3 == " ":
                    cell_3 = player
            elif cell == 4:
                if cell_4 == " ":
                    cell_4 = player
            elif cell == 5:
                if cell_5 == " ":
                    cell_5 = player
            elif cell == 6:
                if cell_6 == " ":
                    cell_6 = player
            elif cell == 7:
                if cell_7 == " ":
                    cell_7 = player
            elif cell == 8:
                if cell_8 == " ":
                    cell_8 = player
            elif cell == 9:
                if cell_9 == " ":
                    cell_9 = player
            else:
                print "Cell already has a character."

            winCheck()
            changePlayer()
            #os.system("cls")
            printBoard()

        choice = raw_input("Want to play again? y/n ")
        if choice == "y":
            playAgain = True
            gameFinished = False
            cell_1 = " "
            cell_2 = " "
            cell_3 = " "
            cell_4 = " "
            cell_5 = " "
            cell_6 = " "
            cell_7 = " "
            cell_8 = " "
            cell_9 = " "
            #os.system("cls")
            printBoard()
        else:
            playAgain = False
            
if __name__ == '__main__':
    main()
