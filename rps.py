#!/usr/bin/env python3.8
from random import randrange
plays=[]

def rock(a,b,c,plays):
    state = randrange(100)
    if state <=a:
        state = 0
    elif state >=b and state<=c:
        state = 1
    else:
        state = 2
    lst = ["rock","paper","scissors"]

    while True:
        item = input("pick rock paper or scissors ")
        
        if item == "rock":
            
            if state==0:
                win = "draw"
            elif state==1:
                 win = "loss"
            else:               
                win = "win"
            break
        elif item == "paper":
            num = 1
            if state==0:
                win = "win"
            elif state==1:
                 win = "draw"
            else:               
                win = "loss"
            break
        elif item == "scissors":
            num = 2
            if state==0:
                win = "loss"
            elif state==1:
                 win = "win"
            else:               
                win = "draw"
            break
        else:
            break
    print("computer played ",lst[state], "you played ", item, " you're ",win )
    plays.append(item)
    return plays
scissors_p = 33
rock_p=33
while True:
    
    #plays = rock(33,34,66,plays)
    plays = rock(scissors_p,scissors_p+1,scissors_p+rock_p,plays)
    ch = input("do you want to play again yes or no ")
    rocks_played = plays.count('rock')
    paper_played = plays.count('paper')
    scissors_played = plays.count('scissors')
    rock_p = int((rocks_played/len(plays))*100)
    paper_p = int((paper_played/len(plays))*100)
    scissors_p = int((scissors_played/len(plays))*100)
    plays = rock(scissors_p,scissors_p+1,scissors_p+rock_p,plays)
    print("rock prob ",scissors_p,"paper",scissors_p+1,scissors_p+rock_p)

    if ch == "y":
        print(plays)
        pass
    else:
        break





