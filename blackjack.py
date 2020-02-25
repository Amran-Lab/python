#!/usr/bin/env python3.8
from cards import card

from random import randint
lst = []

colors = ['heart', 'diamonds', 'spades', 'clubs']
value = ['2','3','4','5','6','7','8','9','10','Ace','Jack','Queen','King']
red = []
for colours in colors:
    for val in value:
        add = [colours,val]
        red.append(add)


def pick():
    picked = len(lst)
    while picked==len(lst):
        pick = randint(0,52)
        if pick not in lst:
            lst.append(red[pick])
            #print(lst,"item", pick)
def clearlst():
    lst = []      




def evaluate(rel):
    count = 0
    ace = 0
    for i in range(len(rel)):
        if rel[i][1] == 'Queen' or rel[i][1] == 'King' or rel[i][1] == 'Jack':
            count += 10
        elif rel[i][1] == 'Ace':
            ace += 1
        else:
            val =  int(rel[i][1])
            count += val
    for i in range(ace):
        if count >12:
            count += 1
        else:
            count += 11
    return count
        






value = 0
while True:
    option = input("1hit \n2.play \n3.stop \n")   
    if option == 'hit':
        pick()
        print(lst)
        
        thing = evaluate(lst)
        if thing >=22:
            print("you went over")
            print(thing)
            break
        print(thing)
    if option == 'play':
        thing = evaluate(lst)
        if thing >=22:
            print("you went over")
            break
        print(thing)
    if option == 'stop':
        break