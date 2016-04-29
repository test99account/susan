#IMPORTING MODULES
import random
#DECLARING VARIABLES
turn = random.randint(1, 2)
if turn == 1:
    xTurn = False
    oTurn = True
elif turn == 2:
    xTurn = True
    oTurn = False
gameTypeLoop = True
susanTurn = 0
a1 = " "
a2 = " "
a3 = " "
b1 = " "
b2 = " "
b3 = " "
c1 = " "
c2 = " "
c3 = " "
#PLAYER 1 OR 2 CHECK
print("Would you like to play singleplayer, with Susan the AI, or multiplayer?")
while gameTypeLoop == True:
    gameType = input(">: ")
    #CHECK FOR SINGLEPLAYER
    if (gameType[:1] == "s") or ("1" in gameType) or ("one" in gameType) or ("single" in gameType) or ("alone" in gameType) or ("single" in gameType) or ("susan" in gameType):
        singleplayer = True
        multiplayer = False
        gameTypeLoop = False
    #CHECK FOR MULTIPLAYER
    elif (gameType[:1] == "m") or ("2" in gameType) or ("two" in gameType) or ("multi" in gameType):
        multiplayer = True
        singleplayer = False
        gameTypeLoop = False
    #NEITHER SINGLEPLAYER OR MULTIPLAYER RETURNED TRUE
    else:
        print("Please choose either 'singleplayer' or 'multiplayer'")
#PRINTING FIRST GRID
print("\n"*32, "   1", "2", "3", "\n", "A ", a1, a2, a3, "\n", "B ", b1, b2, b3, "\n", "C ", c1, c2, c3, "\n"*2)
#CHECKING FOR WIN/DRAW
def turn():
    #DECLARING GLOBAL VARIABLES
    global a1, a2, a3, b1, b2, b3, c1, c2, c3
    #CHECK PLAYER X FOR WIN
    if ((a1 == "x") and (a2 == "x") and (a3 == "x")) or ((b1 == "x") and (b2 == "x") and (b3 == "x")) or ((c1 == "x") and (c2 == "x") and (c3 == "x")) or ((a1 == "x") and (b1 == "x") and (c1 == "x"))  or ((a2 == "x") and (b2 == "x") and (c2 == "x")) or ((a3 == "x") and (b3 == "x") and (c3 == "x")) or ((a1 == "x") and (b2 == "x") and (c3 == "x")) or ((a3 == "x") and (b2 == "x") and (c1 == "x")):
        print("\n"*17, "Player X has won!", "\n")
        print("\n"*14, "   1", "2", "3", "\n", "A ", a1, a2, a3, "\n", "B ", b1, b2, b3, "\n", "C ", c1, c2, c3, "\n"*2)
        wait = input("Press enter to exit")
        exit()
    #CHECK PLAYER O FOR WIN
    elif ((a1 == "o") and (a2 == "o") and (a3 == "o")) or ((b1 == "o") and (b2 == "o") and (b3 == "o")) or ((c1 == "o") and (c2 == "o") and (c3 == "o")) or ((a1 == "o") and (b1 == "o") and (c1 == "o"))  or ((a2 == "o") and (b2 == "o") and (c2 == "o")) or ((a3 == "o") and (b3 == "o") and (c3 == "o")) or ((a1 == "o") and (b2 == "o") and (c3 == "o")) or ((a3 == "o") and (b2 == "o") and (c1 == "o")):
        print("\n"*17, "Player O has won!", "\n")
        print("\n"*14, "   1", "2", "3", "\n", "A ", a1, a2, a3, "\n", "B ", b1, b2, b3, "\n", "C ", c1, c2, c3, "\n"*2)
        wait = input("Press enter to exit")
        exit()
    #CHECK FOR DRAW
    elif (a1 != " ") and (a2 != " ") and (a3 != " ") and (b1 != " ") and (b2 != " ") and (b3 != " ") and (c1 != " ") and (c2 != " ") and (c3 != " "):
        print("\n"*17, "Draw", "\n")
        print("\n"*14, "   1", "2", "3", "\n", "A ", a1, a2, a3, "\n", "B ", b1, b2, b3, "\n", "C ", c1, c2, c3, "\n"*2)
        wait = input("Press enter to exit")
        exit()
#CHECK IF WIN IS POSSIBLE
def priority1():
    #DECLARING GLOBAL VARIABLES
    global a1, a2, a3, b1, b2, b3, c1, c2, c3, oTurn, xTurn
    #CHECK IF IT IS X'S TURN
    if xTurn == True:
        #CHECK IF WIN BY PLAYING A1
        if ((a2 == "x") and (a3 == "x") and (a1 == " ")) or ((b1 == "x") and (c1 == "x") and (a1 == " ")) or ((b2 == "x") and (c3 == "x") and (a1 == " ")):
            a1 = "x"
        #CHECK IF WIN BY PLAYING A2
        elif ((a1 == "x") and (a3 == "x") and (a2 == " ")) or ((b2 == "x") and (c2 == "x") and (a2 == " ")):
            a2 = "x"
        #CHECK IF WIN BY PLAYING A3
        elif ((a1 == "x") and (a2 == "x") and (a3 == " ")) or ((b3 == "x") and (c3 == "x") and (a3 == " ")):
            a3 = "x" 
        #CHECK IF WIN BY PLAYING B1
        elif ((b2 == "x") and (b3 == "x") and (b1 == " ")) or ((a1 == "x") and (c1 == "x") and (b1 == " ")):
            b1 = "x"
        #CHECK IF WIN BY PLAYING B2  
        elif ((b1 == "x") and (b3 == "x") and (b2 == " ")) or ((a1 == "x") and (c1 == "x") and (b2 == " ")) or ((a2 == "x") and (c2 == "x") and (b2 == " ")) or ((a1 == "x") and (c3 == "x") and (b2 == " ")) or ((c1 == "x") and (a3 == "x") and (b2 == " ")):
            b2 = "x"
        #CHECK IF WIN BY PLAYING C1
        elif ((c2 == "x") and (c3 == "x") and (c1 == " ")) or ((a1 == "x") and (b1 == "x") and (c1 == " ")):
            c1 = "x"
        #CHECK IF WIN BY PLAYING C2
        elif ((c1 == "x") and (c3 == "x") and (c2 == " ")) or ((a2 == "x") and (b2 == "x") and (c2 == " ")):
            c2 = "x"
        #CHECK IF WIN BY PLAYING C3
        elif ((c1 == "x") and (c2 == "x") and (c3 == " ")) or ((a3 == "x") and (b3 == "x") and (c3 == " ")):
            c3 = "x"
#CHECK IF BLOCKING ENEMY WIN IS POSSIBLE
def priority2():
    #DECLARING GLOBAL VARIABLES
    global a1, a2, a3, b1, b2, b3, c1, c2, c3, oTurn, xTurn
    #CHECK IF IT IS X'S TURN
    if xTurn == True:
        #CHECK IF WIN BY PLAYING A1
        if ((a2 == "o") and (a3 == "o")) or ((b1 == "o") and (c1 == "o")) or ((b2 == "o") and (c3 == "o")):
            a1 = "x"
            xTurn = False
            oTurn = True
        #CHECK IF WIN BY PLAYING A2
        elif ((a1 == "o") and (a3 == "o")) or ((b2 == "o") and (c2 == "o")):
            a2 = "x"
            xTurn = False
            oTurn = True
        #CHECK IF WIN BY PLAYING A3
        elif ((a1 == "o") and (a2 == "o")) or ((b3 == "o") and (c3 == "o")):
            xTurn = False
            oTurn = True
        #CHECK IF WIN BY PLAYING B1
        elif ((b2 == "o") and (b3 == "o")) or ((a1 == "o") and (c1 == "o")):
            b1 = "x"
            xTurn = False
            oTurn = True
        #CHECK IF WIN BY PLAYING B2  
        elif ((b1 == "o") and (b3 == "o")) or ((a1 == "o") and (c1 == "o")) or ((a2 == "o") and (c2 == "o")) or ((a1 == "o") and (c3 == "o")) or ((c1 == "o") and (a3 == "o")):
            b2 = "x"
            xTurn = False
            oTurn = True
        #CHECK IF WIN BY PLAYING C1
        elif ((c2 == "o") and (c3 == "o")) or ((a1 == "o") and (b1 == "o")):
            c1 = "x"
            xTurn = False
            oTurn = True
        #CHECK IF WIN BY PLAYING C2
        elif ((c1 == "o") and (c3 == "o")) or ((a2 == "o") and (b2 == "o")):
            c2 = "x"
            xTurn = False
            oTurn = True
        #CHECK IF WIN BY PLAYING C3
        elif ((c1 == "o") and (c2 == "o")) or ((a3 == "o") and (b3 == "o")):
            c3 = "x"
            xTurn = False
            oTurn = True
#CHECK IF CENTRE SQUARE IS FREE
def priority3():
    #DECLARING GLOBAL VARIABLES
    global a1, a2, a3, b1, b2, b3, c1, c2, c3, oTurn, xTurn
    #CHECK IF IT IS X'S TURN
    if xTurn == True:
        #CHECK IF B2 IS FREE
        if b2 == " ":
            b2 = "x"
            xTurn = False
            oTurn = True
#CHECK IF CORNER SQUARE IS FREE
def priority4():  
    #DECLARING GLOBAL VARIABLES
    global a1, a2, a3, b1, b2, b3, c1, c2, c3, oTurn, xTurn
    #CHECK IF IT IS X'S TURN
    if xTurn == True:
        #CHECK IF A1 IS FREE
        if a1 == " ":
            a1 = "x"
            xTurn = False
            oTurn = True
        #CHECK IF A3 IS FREE
        elif a3 == " ":
            a3 = "x"
            xTurn = False
            oTurn = True
        #CHECK IF C1 IS FREE
        elif c1 == " ":
            c1 = "x"
            xTurn = False
            oTurn = True
        #CHECK IF C3 IS FREE
        elif c3 == " ":
            c3 = "x"
            xTurn = False
            oTurn = True
def priority5():
    #DECLARING GLOBAL VARIABLES
    global a1, a2, a3, b1, b2, b3, c1, c2, c3, oTurn, xTurn
    #CHECK IF IT IS X'S TURN
    if xTurn == True:
        #CHECK IF A2 IS FREE
        if a2 == " ":
            a2 = "x"
            xTurn = False
            oTurn = True
        #CHECK IF B1 IS FREE
        elif b1 == " ":
            b1 = "x"
            xTurn = False
            oTurn = True
        #CHECK IF B3 IS FREE
        elif b3 == " ":
            b3 = "x"
            xTurn = False
            oTurn = True
        #CHECK IF C2 IS FREE
        elif c2 == " ":
            c2 = "x"
            xTurn = False
            oTurn = True
while True:
    #X'S TURN MULTIPLAYER
    while (xTurn == True) and (multiplayer == True):
        #RUN CHECK FOR WIN/DRAW
        turn()
        #PLAYER INPUT
        x = input("X: ")
        #CHECK IF X INPUT STARTS WITH A
        if x[:1] == "a":
            #CHECK IF X INPUT ENDS WITH  
            if (x[1:] == "1") and (a1 == " "):
                a1 = "x"
                xTurn = False
                oTurn = True
            #CHECK IF X INPUT ENDS WITH  2
            elif (x[1:] == "2") and (a2 == " "):
                a2 = "x"
                xTurn = False
                oTurn = True
            #CHECK IF X INPUT ENDS WITH 3 
            elif (x[1:] == "3") and (a3 == " "):
                a3 = "x"
                xTurn = False
                oTurn = True
        #CHECK IF X INPUT STARTS WITH B
        elif x[:1] == "b":
            #CHECK IF X INPUT ENDS WITH 1
            if (x[1:] == "1") and (b1 == " "):
                b1 = "x"
                xTurn = False
                oTurn = True
            #CHECK IF X INPUT ENDS WITH 2
            elif (x[1:] == "2") and (b2 == " "):
                b2 = "x"
                xTurn = False
                oTurn = True
            #CHECK IF X INPUT ENDS WITH 3
            elif (x[1:] == "3") and (b3 == " "):
                b3 = "x"
                xTurn = False
                oTurn = True
        #CHECK IF X INPUT STARTS WITH C
        elif x[:1] == "c":
            #CHECK IF X INPUT ENDS WITH 1
            if (x[1:] == "1") and (c1 == " "):
                c1 = "x"
                xTurn = False
                oTurn = True
            #CHECK IF X INPUT ENDS WITH 2
            elif (x[1:] == "2") and (c2 == " "):
                c2 = "x"
                xTurn = False
                oTurn = True
            #CHECK IF X INPUT ENDS WITH 3
            elif (x[1:] == "3") and (c3 == " "):
                c3 = "x"
                xTurn = False
                oTurn = True
        #CHECK IF OTURN IS TRUE
        if oTurn == True:
            xTurn = False
            print("\n"*32, "   1", "2", "3", "\n", "A ", a1, a2, a3, "\n", "B ", b1, b2, b3, "\n", "C ", c1, c2, c3, "\n"*2)
    #X'S TURN SINGLEPLAYER
    if (xTurn == True) and (singleplayer == True):
        #RUN CHECK FOR WIN/DRAW
        turn()
        #RUN PRIORITYS
        priority1()
        priority2()
        priority3()
        priority4()
        priority5()
        #RUN CHECK FOR WIN/DRAW
        turn()
        #CHECK IF OTURN IS TRUE
        if oTurn == True:
            xTurn = False
            print("\n"*32, "   1", "2", "3", "\n", "A ", a1, a2, a3, "\n", "B ", b1, b2, b3, "\n", "C ", c1, c2, c3, "\n"*2)
    #O'S TURN
    while oTurn == True:
        #RUN CHECK FOR WIN/DRAW
        turn()
        #PLAYER INPUT
        o = input("O: ")
        #CHECK IF 0 INPUT STARTS WITH A
        if o[:1] == "a":
            #CHECK IF O INPUT ENDS WITH  
            if (o[1:] == "1") and (a1 == " "):
                a1 = "o"
                xTurn = True
            #CHECK IF 0 INPUT ENDS WITH  2
            elif (o[1:] == "2") and (a2 == " "):
                a2 = "o"
                xTurn = True
            #CHECK IF 0 INPUT ENDS WITH 3 
            elif (o[1:] == "3") and (a3 == " "):
                a3 = "o"
                xTurn = True
        #CHECK IF 0 INPUT STARTS WITH B
        elif o[:1] == "b":
            #CHECK IF 0 INPUT ENDS WITH 1
            if (o[1:] == "1") and (b1 == " "):
                b1 = "o"
                xTurn = True
            #CHECK IF 0 INPUT ENDS WITH 2
            elif (o[1:] == "2") and (b2 == " "):
                b2 = "o"
                xTurn = True
            #CHECK IF 0 INPUT ENDS WITH 3
            elif (o[1:] == "3") and (b3 == " "):
                b3 = "o"
                xTurn = True
        #CHECK IF 0 INPUT STARTS WITH C
        elif o[:1] == "c":
            #CHECK IF 0 INPUT ENDS WITH 1
            if (o[1:] == "1") and (c1 == " "):
                c1 = "o"
                xTurn = True
            #CHECK IF 0 INPUT ENDS WITH 2
            elif (o[1:] == "2") and (c2 == " "):
                c2 = "o"
                xTurn = True
            #CHECK IF 0 INPUT ENDS WITH 3
            elif (o[1:] == "3") and (c3 == " "):
                c3 = "o"
                xTurn = True
        #CHECK IF XTURN IS TRUE
        if xTurn == True:
            oTurn = False
            if multiplayer == True:
                print("\n"*32, "   1", "2", "3", "\n", "A ", a1, a2, a3, "\n", "B ", b1, b2, b3, "\n", "C ", c1, c2, c3, "\n"*2)
