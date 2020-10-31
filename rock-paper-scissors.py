from random import randint

print("Let's start the game")

lst = ['rock', 'paper', 'scissors']

computer_score = 0
user_score = 0

while True:
    if computer_score == 3 or user_score == 3:
        break
    
    computer = lst[randint(0,2)]
    
    user = input("Please enter your weapon (Rock, Paper, Scissors):  ").lower()

    if computer == user:
        print("tie - no one wins")
    
    elif user == "rock":
        if computer == "paper":
            print("paper beats rock - computer wins")
            computer_score += 1
        else:
            print("rock beats scissors - user wins")
            user_score += 1

# to be continued...

                  

