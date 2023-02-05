import time
import random

#Login & Register
allowed = False

def intro():
    global selection
    print("Welcome to the Dice Game")
    time.sleep(.5)
    selection = str(input("Do you want to login or register (login or reg): "))
    if selection != "login" and selection != "reg":
        intro()
    else:
        auth(selection)

def auth(selection):
    global username
    if selection == "login":
        print("Please enter your username")
        username = input("")
        time.sleep(.2)
        print("Please enter your password")
        password = input("")
        login(username,password)
    else:
        print("Please enter the username you want to register")
        username = input("")
        time.sleep(.2)
        print("Please enter the password you want to register")
        password = input("")
        register(username,password)

def login(username,password):
    global allowed
    allow = False
    f = open("Register.txt","r")
    for i in f:
        a,b = i.split(",")
        b = b.strip()
        if a == username and b == password:
            allow = True     
    if allow == True:
        f.close()
        permission()
    else:
        print("Incorrect Username or Password")
        f.close()
        intro()
        
def register(username,password):
    f = open("Register.txt","a")
    f.write("\n" + username + "," + password)
    f.close()
    permission()

def permission():
    allowed = True
    if allowed == True:
        print("You have been authorised\n")
        time.sleep(1)
intro()
