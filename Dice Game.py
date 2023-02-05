#Ilhaam Ifarm
#24/09/2021
#Dice Game


#import
from time import sleep
from random import randint

#Reset
allowed = False
player2 = False
auth2 = False
work = False
dos = False
compvplayer = False
playervplayer = False

P1score = 0
Cscore = 0
P2score = 0

P2username = "none"
P2password = "none"
P1selection1 = "none"

#Login and Register
def intro(): 
    global P1selection 
    print("Welcome to the Dice Game")
    sleep(.5)
    P1selection = str(input("Do you want to login or register (login or reg): "))
    if P1selection != "login" and P1selection != "reg":
        intro()
    else:
        auth(P1selection)

def startup():
    print("\nPlayer 2 has been authorised\n")
    sleep(.5)
    print("\nWelcome back",P2username,"\n")
    players()

def login(P1username,P1password):
    global allow
    allow = False
    if P2username == P1username and P2password == P1password:
        print("Sorry but you can't use the same account\n")
        auth(P1selection)
    else:
        if player2 == True and auth2 == True:
            p = open("Register.txt","r")
            for i in p:
                c,d = i.split(",")
                d = d.strip()
                if c == P2username and d == P2password:
                    allow = True
        else:
            f = open("Register.txt","r")
            for i in f:
                a,b = i.split(",")
                b = b.strip()
                if a == P1username and b == P1password:
                    allow = True
                    work = True
                    
        if allow == True and auth2 == True:
            p.close
            startup()
                
        elif allow == True and auth2 != True:
            f.close()
            permission()
        else:
            sleep(.5)
            print("\nIncorrect username or password\n")
            intro()
        
def auth(P1selection):
    global P1username
    global P1password
    global P2username
    global P2password
    if P1selection == "login" and player2 != True:
        print("Please enter your username")
        P1username = input("")
        sleep(.2)
        print("Please enter your password")
        P1password = input("")
        P1selection = "none"
        login(P1username,P1password)
        
    elif P1selection1 == "login" and player2 == True:
        print("Please enter your username")
        P2username = input("")
        sleep(.2)
        print("Please enter your password")
        P2password = input("")
        login(P1username,P1password)
        
    elif P1selection1 == "reg" and work == True:
        print("Please enter the username you want to register")
        P2username = input("")
        sleep(.2)
        print("Please enter the password you want to register")
        P2password = input("")
        register(P1username,P1password)
    elif P1selection == "reg" and work == False:
        print("Please enter the username you want to register")
        P1username = input("")
        sleep(.2)
        print("Please enter the password you want to register")
        P1password = input("")
        register(P1username,P1password)

def register(P1username,P1password):
    if auth2 == True:
        p = open("Register.txt","a")
        p.write("\n" + P2username + "," + P2password)
        p.close()
        startup()
    else:
        f = open("Register.txt","a")
        f.write("\n" + P1username + "," + P1password)
        f.close()
        work = True
        permission()
        
def permission():
    allowed = True
    if allowed == True:
        print("You have been authorised\n")
        sleep(.5)
        print("\nWelcome back",P1username,"\n")
        sleep(1)

#Leaderboard
def leaderboardwrite():
    if compvplayer == True:
        file = open("Leaderboard.txt","a")
        file.write("\n" + (str(P1score)) + "," + P1username)
        file.close()  
        file2 = open("Leaderboard.txt","a")
        file2.write("\n" + (str(Cscore)) + "," + P2username)
        file2.close()
        leaderboardread()
    elif playervplayer == True:
        file3 = open("Leaderboard.txt","a")
        file3.write("\n" + (str(P1score)) + " points ," + P1username)
        file3.close()
        file4 = open("Leaderboard.txt","a")
        file4.write("\n" + (str(P2score)) + " points ," + P2username)
        file4.close()
        leaderboardread()
    else:
        leaderboardread()
        
def leaderboardread():
    file5 = open("Leaderboard.txt","r")
    read = file5.readlines()
    sort = sorted(read,reverse = True)
    print("Do you want to print the leaderboard? (Yes or No): ")
    answer = str(input(""))
    answer = answer.lower()
    sleep(.5)
    
    if answer == "yes":
        print("\nThe top 5 scores:\n")
        for line in range (5):
            print(str(line + 1) + "\tPoints: " + str(sort[line]))

    else:
        print("\nThat's alright\n")

#Game
intro()

#Rules
print("Do you want to see the rules?")
sleep(.5)
print("\nType 'r' to open rules\nor press enter to continue")
rule = str(input(""))
if rule == "r":
    print("\nYou and the second player have to roll two dices 5 times.\nIf the total of the 2 dices is an even number,\nthen 10 points will be added to your total.\nAlthough if your total is an odd number, 5 points will be subtracted.\nAlso, if a double is rolled\nthen another die will be rolled and added to the score. \nWhoever has the largest score at the end will win. \nAlthough if the two players have the same score, a duel will occur. \nTwo dices will be rolled and who ever has the most \nwin the entire game.")  
    sleep(5)
    print("\nPress 'enter' to continue")
    press = input("")
    
    if press == "":
        print("Time to start the game")
else:
    print("Time to start the game")

#Player P1selection

def turns():
    global P1score
    global turn
    roll = "y"
    P1score = 0
    turn = 0
    while roll == "y" and turn < 5:
        luckydierolled = False
        die_1 = randint(1,6)
        die_2 = randint(1,6)
        die_3 = randint(1,6)
        print("Press enter to roll")
        input("")
        sleep(.8)
        print("You rolled a",die_1,"and a",die_2)
        if (die_1 - die_2) == 0:
            luckydierolled = True
            sleep(0.5)
            print("A double has been rolled")
            sleep(.5)
            print("Press enter to roll the lucky die")
            input("")
            sleep(0.5)
            print("You rolled a",die_3)
            P1score = P1score + die_3
            turn = turn + 1
            sleep(.6)
            print("\nCurrently you have",P1score,"points\n")
        if luckydierolled == False and (die_1 + die_2) % 2 == 0:
            sleep(.5)
            print("Your total amount has added to an even number.\n10 extra points will be added")
            P1score = P1score + (die_1 + die_2)
            P1score = P1score + 10
            turn = turn + 1
            sleep(.4)
            print("\nCurrently you have",P1score,"points\n")
        if (die_1 + die_2) % 2 != 0:
            sleep(.5)
            print("Your total amount has added to an odd number.\n5 points will be subtracted")
            P1score = P1score + (die_1 + die_2)
            P1score = P1score - 5
            sleep(.4)
            if P1score <= 0:
                turn = turn + 1
                P1score = 0
                sleep(0.4)
                print("Your P1score is bellow 0")
            else:
                print("\nCurrently you have",P1score,"points\n")
                turn = turn + 1
    if P1score >= 50:
        print("Well done, that is quite hard to beat")
        roll1 = "y"
        computer()
    else:
        print("You could have done a bit better")
        roll1 = "y"
        computer()


def total():
    global P1score
    global P2score
    global playervplayer
    if P1score != P2score:
        if P1score < P2score:
            print("\n",P2username,"has won the title on the leaderboard\n")
            playervplayer = True
            P1score = str(P1score)
            P2score = str(P2score)
            leaderboardwrite()
            
        else:
            print("\n",P1username,"has won the title on the leaderboard\n")
            playervplayer = True
            P1score = str(P1score)
            scoore4 = str(P2score)
            leaderboardwrite()
            
    else:
        print("DUEL")
        sleep(.5)
        print("Roll the die and whoever gets the most wins")
        sleep(1)
        duel = False
        duelturns = 0
        while duel == False:
            print("\nPress enter to roll")
            input("")
            dueldie = randint(1,6)
            dueldie2 = randint(1,6)
            print("\nYou have rolled a",dueldie,"\n")
            player1dueldie = dueldie
            sleep(2)
            print("\nNow",P2username,"press enter to roll the die\n")
            input("")
            sleep(.3)
            print("You have rolled a",dueldie2)
            sleep(2)
            player1dueldie = player2dueldie
            if player1dueldie < player2dueldie:
                print(P2username,"has won the title on the leaderboard")
                P1score = P1score
                Cscore = P2score
                duel = True
                playervplayer = True
                leaderboardwrite()
            elif player1dueldie > player2dueldie:
                print(P1username,"has won the title on the leaderboard")
                P1score = P1score
                Cscore = P2score
                duel = True
                playervplayer = True
                leaderboardwrite()
            else:
                print("You both rolled the same")
                sleep(.5)
                total()

#Player vs Player
def player2turn():
    global P2score
    global turn4
    roll = "y"
    P2score = 0
    turn4 = 0
    while roll == "y" and turn4 < 5:
        luckydierolled  = False
        die_1 = randint(1,6)
        die_2 = randint(1,6)
        die_3 = randint(1,6)
        print("Press enter to roll")
        input("")
        sleep(.8)
        print("You rolled a",die_1,"and a",die_2)
        if (die_1 - die_2) == 0:
            luckydierolled = True
            sleep(0.5)
            print("A double has been rolled")
            sleep(.5)
            print("Press enter to roll the lucky die")
            input("")
            sleep(0.5)
            print("You rolled a",die_3)
            P2score = P2score + die_3
            turn4 = turn4 + 1
            sleep(.6)
            print("\nCurrently you have",P2score,"points\n")
        if luckydierolled == False and (die_1 + die_2) % 2 == 0:
            sleep(.5)
            print("Your total amount has added to an even number.\n10 extra points will be added")
            P2score = P2score + (die_1 + die_2)
            P2score = P2score + 10
            turn4 = turn4 + 1
            sleep(.4)
            print("\nCurrently you have",P2score,"points\n")
        if (die_1 + die_2) % 2 != 0:
            sleep(.5)
            print("Your total amount has added to an odd number.\n5 points will be subtracted")
            P2score = P2score + (die_1 + die_2)
            P2score = P2score - 5
            sleep(.4)
            if P2score <= 0:
                turn4 = turn4 + 1
                P2score = 0
                sleep(0.4)
                print("Your P1score is bellow 0")
            else:
                print("\nCurrently you have",P2score,"points\n")
                turn4 = turn4 + 1
    sleep(1)
    print("\nAt the end of these 5 rounds,",P2username,"earned",P2score,"points\n")
    sleep(2)
    total()
    
def players():
    sleep(.4)
    print("With this gamemode, the players will do all 5 rounds and then swap turn.\nAgain, whoever has the largest P1score will be put on the leaderboard.\n")
    sleep(1)
    print("\nPlayer 1 start\n")
    global P1score
    global turn3
    roll = "y"
    P1score = 0
    turn3 = 0
    while roll == "y" and turn3 < 5:
        luckydierolled = False
        die_1 = randint(1,6)
        die_2 = randint(1,6)
        die_3 = randint(1,6)
        print("Press enter to roll")
        input("")
        sleep(.8)
        print("You rolled a",die_1,"and a",die_2)
        if (die_1 - die_2) == 0:
            luckydierolled = True
            sleep(0.5)
            print("A double has been rolled")
            sleep(.5)
            print("Press enter to roll the lucky die")
            input("")
            sleep(0.5)
            print("You rolled a",die_3)
            P1score = P1score + die_3
            turn3 = turn3 + 1
            sleep(.6)
            print("\nCurrently you have",P1score,"points\n")
        if luckydierolled == False and (die_1 + die_2) % 2 == 0:
            sleep(.5)
            print("Your total amount has added to an even number.\n10 extra points will be added")
            P1score = P1score + (die_1 + die_2)
            P1score = P1score + 10
            turn3 = turn3 + 1
            sleep(.4)
            print("\nCurrently you have",P1score,"points\n")
        if (die_1 + die_2) % 2 != 0:
            sleep(.5)
            print("Your total amount has added to an odd number.\n5 points will be subtracted")
            P1score = P1score + (die_1 + die_2)
            P1score = P1score - 5
            sleep(.4)
            if P1score <= 0:
                turn3 = turn3 + 1
                P1score = 0
                sleep(0.4)
                print("Your P1score is bellow 0")
            else:
                print("\nCurrently you have",P1score,"points\n")
                turn3 = turn3 + 1
            
    sleep(1)
    print("\nAt the end of these 5 rounds,",P1username,"earned",P1score,"points\n")
    sleep(2)
    print("\nNow it is",P2username,"'s turn")
    player2turn()

#Player vs Computer
def computer():
    global compvplayer
    global Cscore
    turn1 = 0
    Cscore = 0
    roll1 = "y"
    print("It is now the computers turn")
    while roll1 == "y" and turn1 < 5:
        luckydierolled = False
        die_4 = randint(1,6)
        die_5 = randint(1,6)
        die_6 = randint(1,6)
        sleep(1)
        print("\nThe computer is rolling the dices\n")
        sleep(2)
        print("It has landed on a ",die_4,"and a",die_5)
        if (die_4 - die_5) == 0:
            luckydierolled = True
            print("The computer has landed on a Lucky die")
            sleep(2)
            print("The lucky die rolled a",die_6)
            sleep(2)
            Cscore = Cscore + die_6
            turn1 = turn1 + 1
            print("\nThe computer has",Cscore,"points\n")
        if luckydierolled == False and (die_4 + die_5) % 2 == 0:
            print("The total is an even number")
            Cscore = Cscore + (die_4 + die_5)
            Cscore = Cscore + 10
            turn1 = turn1 + 1
            sleep(2)
            print("\nThe computer has",Cscore,"points currently\n")
        if (die_4 + die_5) % 2 != 0:
            print("The total is an odd number")
            Cscore = Cscore + (die_4 + die_5)
            Cscore = Cscore - 5
            turn1 = turn1 + 1
            sleep(2)
            if P1score <= 0:
                print("The computers P1score is less then 0")
            else:
                print("\nThe computer has",Cscore,"points currently\n")
                if P1score == Cscore:
                    print("DUEL")
                    sleep(.5)
                    print("Roll the die and whoever gets the most wins")
                    sleep(1)
                    due1 = False
                    duelturns = 0
                    while duel == False:
                        print("\nPress enter to roll")
                        input("")
                        dueldie = randint(1,6)
                        dueldie2 = randint(1,6)
                        print("\nYou have rolled a",dueldie,"\n")
                        player1dueldie = dueldie
                        sleep(2)
                        print("\nNow the computer will roll the die\n")
                        input("")
                        sleep(.3)
                        print("The comouter has rolled a",dueldie2)
                        computerdueldie = dueldie2
                        sleep(2)
            
                    if player1dueldie > computerdueldie:
                        print(P1username,"has won the title on the leaderboard")
                        duel = True
                        compvplayer = True
                        leaderboardwrite()
                    elif player1dueldie < computerdueldie:
                        print("Unlucky, but computer has won")
                        duel = True
                        compvplayer = True
                        leaderboardwrite()
                    else:
                        print("You both rolled the same")
                        sleep(.5)
                        total()

    if P1score != Cscore:
        if P1score < Cscore:
            print("Unlucky",P1username,"lost to the computer")
            compvplayer = True
            leaderboardwrite()
        else:
            print("Congratulations",username,". You have won a place on the leaderboard")
            compvplayer = True
            leaderboardwrite()


sleep(.6)

#Player P1selection
while dos == False:
    player = str(input("Do you want to play with another Player or a Computer? (Player or Computer): "))

    if player in ("player","play"):
        print("You have selected to play with another player\n")
        sleep(.5)
        P1selection1 = str(input("Player 2, Do you want to login or register (Login or Reg): "))
        player2 = True
        auth2 = True
        work = True
        dos = True
        auth(P1selection)
    
    elif player in ("computer","comp"):
        print("You have selected to play with a computer\n")
        dos = True
        turns()
    
    else:
        print("Wrong answer")
        dos = False
#end
