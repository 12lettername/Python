import random

def computer_hand():
    val = random.randint(1,3)
    comp = ""
    if val ==1:
        comp = "Rock"
    elif val ==2:
        comp ="Paper"
    elif val == 3:
        comp = "Scissors"
    return comp

def user_hand():
    user = ""
    while True:
        choice = input("Enter 'r' for rock, 'p' for paper and 's' for scissors")
        if choice =="r":
            user = "Rock"
        elif choice =="p":
            user = "Paper"
        elif choice =="s":
            user = "Scissors"
        if user in ["Rock","Paper","Scissors"]:
            return user
            break
        else:
            print("Invalid Choice! Try Again!")

def check(comp,user):
    if comp =="Rock" and user =="Paper" or comp =="Paper" and user =="Scissors" or comp =="Scissors" and user =="Rock":
        print("The computer's choice: ",comp)
        print("The user has won!")

    else:
        print("The computer's choice: ",comp)
        print("The computer has won")

while True:
    computer = computer_hand()
    user = user_hand()
    if computer == user:
        print("The computer's choice: ",computer)
        print("Its A TIE! Play Again!")
    else:
        check(computer,user)
        break