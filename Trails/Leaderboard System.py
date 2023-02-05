#Leaderrboard
#28/09/2021

from time import sleep


score3 = "50"
score4 = "20"

username = "Ilhaam"
username1 = "Rasfik"

playervplayer = True
compvplayer = False


def leaderboardwrite():
    if compvplayer == True:
        score = (str(score))
        score1 = (str(score))
        file = open("Leaderboard.txt","a")
        file.write("\n" + score + "," + username)
        file.close()  
        file2 = open("Leaderboard.txt","a")
        file2.write("\n" + score1 + "," + username1)
        file2.close()
        leaderboardread()
    elif playervplayer == True:
        file3 = open("Leaderboard.txt","a")
        file3.write("\n" + score3 + " points ," + username)
        file3.close()
        file4 = open("Leaderboard.txt","a")
        file4.write("\n" + score4 + " points ," + username1)
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
            print(str(line + 1) + "\t-\t" + str(sort[line]))

    else:
        print("\nThat's alright\n")
                  

    sleep(1)
    print("\nDo you want to play the game again? (Yes or No): ")
    again = str(input(""))
    again = again.lower()
    if again == "yes":
        print("\nThen you must\n")
        sleep(2)
        #intro()
    else:
        print("\nI'll see you soon\n")
        sleep(.5)

leaderboardwrite()
