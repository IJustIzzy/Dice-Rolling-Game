#Ilhaam Ifarm
#24/09/2021
#Dice Game

#import
from time import sleep
from random import randint

#Reset #To change everything to 0
allowed = False
player2 = False
auth2 = False
work = False
dos = False
compvplayer = False
playervplayer = False

score = 0
score1 = 0
score3 = 0
score4 = 0

username1 = "none"
password1 = "none"
selection1 = "none"

#Login and Register
def intro(): #Function to recall whenever I need
    global selection #So I can use "selection" outside of the function
    print("Welcome to the Dice Game") #Print is to output onto the shell
    sleep(.5) #Pause
    selection = str(input("Do you want to login or register (login or reg): ")) #Input to allow the user to insert their own information
    if selection != "login" and selection != "reg": #If command to check if the user inputed the correct thing
        intro() #Reverts to the beginning if there is no of the above
    else: #If not then do this
        auth(selection) #Sends to the authorification stage

def startup(): #This is for the second players login (later)
    print("\nPlayer 2 has been authorised\n") #Print
    sleep(.5) #Pause
    print("\nWelcome back",username1,"\n") #Print
    players() #Sends it to the pvp gamemode

def login(username,password): #Takes the "username" and "password" that was inputed to be used in this function
    global allow #Global
    allow = False #The user is only allowed once "allow" becomes True
    if username1 == username and password1 == password: #If the second players login details are the same as player 1 then it won't allow the user to pass
        print("Sorry but you can't use the same account\n") #Print
        auth(selection) #Sends back to the authorification
    else: #For player 2
        if player2 == True and auth2 == True: #To disallow this triggering when Player 1 signs in
            p = open("Register.txt","r") #Opens the file called "Register.txt" is the directory #It is in "r" mode which stands for read
            for i in p: #For loop to go in through all the lines to check for a match of the username and password
                c,d = i.split(",") #removes the "," of the two new variables
                d = d.strip() #Removes all the unwanted spaces before and after "d"
                if c == username1 and d == password1: #If "c" and "d" match with the entered "username" and "password"
                    allow = True #Then allow is True
    else: #For Player 1
            f = open("Register.txt","r") #Open file
            for i in f: #For loop
                a,b = i.split(",") #Remove the ","
                b = b.strip() #Removes the unwanted spaces between
                if a == username and b == password: #If they match
                    allow = True #Allow is True
                    work = True #Work is True #To stop Player 2 info from mixing up later on
                    
        if allow == True and auth2 == True:
            p.close
            startup()
                
        elif allow == True and auth2 != True:
            f.close()
            permission()
        else:
            sleep(.5)
            print("\nIncorrect Username or Password\n")
            intro()
        
def auth(selection):
    global username
    global password
    global username1
    global password1
    if selection == "login" and player2 != True:
        print("Please enter your username")
        username = input("")
        sleep(.2)
        print("Please enter your password")
        password = input("")
        selection = "none"
        login(username,password)
        
    elif selection1 == "login" and player2 == True:
        print("Please enter your username")
        username1 = input("")
        sleep(.2)
        print("Please enter your password")
        password1 = input("")
        login(username,password)
        
    elif selection1 == "reg" and work == True:
        print("Please enter the username you want to register")
        username1 = input("")
        sleep(.2)
        print("Please enter the password you want to register")
        password1 = input("")
        register(username,password)
    elif selection == "reg" and work == False:
        print("Please enter the username you want to register")
        username = input("")
        sleep(.2)
        print("Please enter the password you want to register")
        password = input("")
        register(username,password)

def register(username,password):
    if auth2 == True:
        p = open("Register.txt","a")
        p.write("\n" + username1 + "," + password1)
        p.close()
        startup()
    else:
        f = open("Register.txt","a")
        f.write("\n" + username + "," + password)
        f.close()
        work = True
        permission()
        
def permission():
    allowed = True
    if allowed == True:
        print("You have been authorised\n")
        sleep(.5)
        print("\nWelcome back",username,"\n")
        sleep(1)

#Leaderboard
def leaderboardwrite():
    if compvplayer == True:
        file = open("Leaderboard.txt","a")
        file.write("\n" + (str(score)) + "," + username)
        file.close()  
        file2 = open("Leaderboard.txt","a")
        file2.write("\n" + (str(score1)) + "," + username1)
        file2.close()
        leaderboardread()
    elif playervplayer == True:
        file3 = open("Leaderboard.txt","a")
        file3.write("\n" + (str(score3)) + " points ," + username)
        file3.close()
        file4 = open("Leaderboard.txt","a")
        file4.write("\n" + (str(score4)) + " points ," + username1)
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
                  

    sleep(1)
    print("\nDo you want to play the game again? (Yes or No): ")
    again = str(input(""))
    again = again.lower()
    if again == "yes":
        print("\nThen you must\n")
        sleep(2)
        intro()
    else:
        print("\nI'll see you soon\n")
        sleep(.5)

#Game
intro()

#Rules
print("Do you want to know the rules?")
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

#Player selection

def turns():
    global score
    global turn
    roll = "y"
    score = 0
    turn = 0
    while roll == "y" and turn < 5:
        luckydierolled = False
        die_1 = randint(1,6)
        die_2 = randint(1,6)
        die_3 = randint(1,6)
        print("Press enter to continue")
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
            score = score + die_3
            turn = turn + 1
            sleep(.6)
            print("\nCurrently you have",score,"points\n")
        if luckydierolled == False and (die_1 + die_2) % 2 == 0:
            sleep(.5)
            print("Your total amount has added to an even number.\n10 extra points will be added")
            score = score + (die_1 + die_2)
            score = score + 10
            turn = turn + 1
            sleep(.4)
            print("\nCurrently you have",score,"points\n")
        if (die_1 + die_2) % 2 != 0:
            sleep(.5)
            print("Your total amount has added to an odd number.\n5 points will be subtracted")
            score = score + (die_1 + die_2)
            score = score - 5
            sleep(.4)
            if score <= 0:
                turn = turn + 1
                score = 0
                sleep(0.4)
                print("Your score is bellow 0")
            else:
                print("\nCurrently you have",score,"points\n")
                turn = turn + 1
    if score >= 50:
        print("Well done, that is quite hard to beat")
        roll1 = "y"
        computer()
    else:
        print("You could have done a bit better")
        roll1 = "y"
        computer()


def total():
    global score3
    global score4
    global playervplayer
    if score3 != score4:
        if score3 < score4:
            print("\n",username1,"has won the title on the leaderboard\n")
            playervplayer = True
            score3 = str(score3)
            score4 = str(score4)
            leaderboardwrite()
            
        else:
            print("\n",username,"has won the title on the leaderboard\n")
            playervplayer = True
            score3 = str(score3)
            scoore4 = str(score4)
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
            print("\nNow",username1,"press enter to roll the die\n")
            input("")
            sleep(.3)
            print("You have rolled a",dueldie2)
            sleep(2)
            player1dueldie = player2dueldie
            if player1dueldie < player2dueldie:
                print(username1,"has won the title on the leaderboard")
                score = score3
                score1 = score4
                duel = True
                playervplayer = True
                leaderboardwrite()
            elif player1dueldie > player2dueldie:
                print(username,"has won the title on the leaderboard")
                score = score3
                score1 = score4
                duel = True
                playervplayer = True
                leaderboardwrite()
            else:
                print("You both rolled the same")
                sleep(.5)
                total()

#Player vs Player
def player2turn():
    global score4
    global turn4
    roll = "y"
    score4 = 0
    turn4 = 0
    while roll == "y" and turn4 < 5:
        luckydierolled  = False
        die_1 = randint(1,6)
        die_2 = randint(1,6)
        die_3 = randint(1,6)
        print("Press enter to continue")
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
            score4 = score4 + die_3
            turn4 = turn4 + 1
            sleep(.6)
            print("\nCurrently you have",score4,"points\n")
        if luckydierolled == False and (die_1 + die_2) % 2 == 0:
            sleep(.5)
            print("Your total amount has added to an even number.\n10 extra points will be added")
            score4 = score4 + (die_1 + die_2)
            score4 = score4 + 10
            turn4 = turn4 + 1
            sleep(.4)
            print("\nCurrently you have",score4,"points\n")
        if (die_1 + die_2) % 2 != 0:
            sleep(.5)
            print("Your total amount has added to an odd number.\n5 points will be subtracted")
            score4 = score4 + (die_1 + die_2)
            score4 = score4 - 5
            sleep(.4)
            if score4 <= 0:
                turn4 = turn4 + 1
                score4 = 0
                sleep(0.4)
                print("Your score is bellow 0")
            else:
                print("\nCurrently you have",score4,"points\n")
                turn4 = turn4 + 1
    sleep(1)
    print("\nAt the end of these 5 rounds,",username1,"earned",score4,"points\n")
    sleep(2)
    total()
    
def players():
    sleep(.4)
    print("With this gamemode, the players will do all 5 rounds and then swap turn.\nAgain, whoever has the largest score will be put on the leaderboard.\n")
    sleep(1)
    print("\nPlayer 1 start\n")
    global score3
    global turn3
    roll = "y"
    score3 = 0
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
            score3 = score3 + die_3
            turn3 = turn3 + 1
            sleep(.6)
            print("\nCurrently you have",score3,"points\n")
        if luckydierolled == False and (die_1 + die_2) % 2 == 0:
            sleep(.5)
            print("Your total amount has added to an even number.\n10 extra points will be added")
            score3 = score3 + (die_1 + die_2)
            score3 = score3 + 10
            turn3 = turn3 + 1
            sleep(.4)
            print("\nCurrently you have",score3,"points\n")
        if (die_1 + die_2) % 2 != 0:
            sleep(.5)
            print("Your total amount has added to an odd number.\n5 points will be subtracted")
            score3 = score3 + (die_1 + die_2)
            score3 = score3 - 5
            sleep(.4)
            if score3 <= 0:
                turn3 = turn3 + 1
                score3 = 0
                sleep(0.4)
                print("Your score is bellow 0")
            else:
                print("\nCurrently you have",score3,"points\n")
                turn3 = turn3 + 1
            
    sleep(1)
    print("\nAt the end of these 5 rounds,",username,"earned",score3,"points\n")
    sleep(2)
    print("\nNow it is",username1,"'s turn")
    player2turn()

#Player vs Computer
def computer():
    global compvplayer
    global score1
    turn1 = 0
    score1 = 0
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
            score1 = score1 + die_6
            turn1 = turn1 + 1
            print("\nThe computer has",score1,"points\n")
        if luckydierolled == False and (die_4 + die_5) % 2 == 0:
            print("The total is an even number")
            score1 = score1 + (die_4 + die_5)
            score1 = score1 + 10
            turn1 = turn1 + 1
            sleep(2)
            print("\nThe computer has",score1,"points currently\n")
        if (die_4 + die_5) % 2 != 0:
            print("The total is an odd number")
            score1 = score1 + (die_4 + die_5)
            score1 = score1 - 5
            turn1 = turn1 + 1
            sleep(2)
            if score <= 0:
                print("The computers score is less then 0")
            else:
                print("\nThe computer has",score1,"points currently\n")
                if score == score1:
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
                        print(username,"has won the title on the leaderboard")
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

    if score != score1:
        if score < score1:
            print("Unlucky",username,"lost to the computer")
            compvplayer = True
            leaderboardwrite()
        else:
            print("Congratulations",username,". You have won a place on the leaderboard")
            compvplayer = True
            leaderboardwrite()


sleep(.6)

#Player Selection
while dos == False:
    player = str(input("Do you want to play with another Player or a Computer? (Player or Computer): "))

    if player == "player" or player == "play":
        print("You have selected to play with another player\n")
        sleep(.5)
        selection1 = str(input("Player 2, Do you want to login or register (Login or Reg): "))
        player2 = True
        auth2 = True
        work = True
        dos = True
        auth(selection)
    
    elif player == "comp" or player == "computer":
        print("You have selected to play with a computer\n")
        dos = True
        turns()
    
    else:
        print("Wrong answer")
        dos = False
#end
