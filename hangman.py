#!/usr/bin/env python3.8




def play(word,letter,guess,r_count,f_count):
    letter_in_word = False
    while True:
        if letter in word:
            pos = word.find(letter)
            guess[pos]=letter
            word = word[:pos] +"."+word[(pos+1):]
            letter_in_word = True
            r_count += 1
        else:
            break
    if letter_in_word == True:
        print(guess)

    else:
        f_count += 1
        print("you have guessed incorrectly ", f_count)
    return word,guess,r_count,f_count



words = ["troop","talk","regular","reach","shaft"]
number = input("pick a word 1-5 ")
val=int(number)-1
word = words[val]
print(word,"word selected")
r_count = 0
f_count = 0
guess= []
for i in range(len(word)):
    guess.append("_")
while True:
    letter = input("pick a letter ")
    word,guess,r_count,f_count = play(word,letter,guess,r_count,f_count)
    if r_count == len(word):
        print("well done")
        break
    elif f_count == 4:
        print("ran out of attempts")
        break






















"""word = words[val]
game= True                    #if penalty reaches 10 goes false
penalty = 0
guess = []
for i in range(len(word)):
    guess.append("_")
print(guess)
lst = []
def play(word,):
    check = input("guess a letter ")
    flag = False
    while True:
        if check in word:
            word.count(check)
            place = word.find(check)
            guess[place]=check
            lst.append(check)
            flag = True
            word = word[:place] +"."+word[(place+1):]
            
        else:
            break
    if flag == True:
        print(guess)
        return 1
    else:
        print("not in word")
        return 0
    

while True:
    count += play(word)

    if len(lst) == len(word):
        print("you've guessed correct")
        break
    elif count==10:
        print("you've ran out of guesses")
    else:
        pass"""



