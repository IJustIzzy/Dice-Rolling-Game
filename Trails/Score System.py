import random

player1score = 0
player2score = 0
turn = 0

def turns():
    global score
    roll = "y"
    score = 0
    turn = 0
    while roll == "y" and turn < 5:
        die_1 = random.randint(1,6)
        die_2 = random.randint(1,6)
        die_3 = random.randint(1,6)
        print("Press enter to continue")
        input("")
        print("You rolled a",die_1,"and a",die_2)
        if (die_1 + die_2) % 2 == 0:
            print("Your total amount has added to an even number.\n10 extra points will be added")
            score = score + (die_1 + die_2)
            score = score + 10
            turn = turn + 1
        if (die_1 + die_2) % 2 != 0:
            print("Your total amount has added to an odd number.\n5 points will be subtracted")
            score = score + (die_1 + die_2)
            score = score - 5
            turn = turn + 1
            if score <= 0:
                turn = turn + 1
                score = 0
                print("Your score is bellow 0")
                print("Press enter to continue")
                input("")
        if (die_1 - die_2) == 0:
            turn = turn + 1
            print("A double has been rolled")
            print("Press enter to roll the lucky die")
            input("")
            print("You rolled a",die_3)
            score = score + die_3
            
            

turns()


