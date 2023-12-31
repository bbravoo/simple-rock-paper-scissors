import random
import sys
print("Hello! Welcome to Rock, Paper, Scissors")
print("Please type R, P, or S")
player= input()
options= [1, 2, 3]
computer = random.choice(options)
if player=='R' :
    if computer==1:
        print("Tie! Hit run to play again")
        sys.exit()
    if computer == 2:
        print("Paper! You lose! Hit run to play again")
        sys.exit()
    if computer == 3:
        print("Scissors! You win! Hit run to play again")
        sys.exit()
if player == 'P':
    if computer==1:
        print("Rock! You win! Hit run to play again")
        sys.exit()
    if computer == 2:
        print("Tie! Hit run to play again")
        sys.exit()
    if computer == 3:
        print("Scissors! You lose! Hit run to play again")
        sys.exit()
if player == 'S':
    if computer==1:
        print("Rock! You lose! Hit run to play again")
        sys.exit()
    if computer == 2:
        print("Paper! You win! Hit run to play again")
        sys.exit()
    if computer == 3:
        print("Tie! Hit run to play again")
        sys.exit()
    
