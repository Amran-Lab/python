#!/usr/bin/env python3.8
def guess():
    #print("hello")
    for i in range(1,100):
        
        
        check = input(" is your number "+str(i)+" if so type y ")
        if check == "y":
            print("your number is", i)
            break
        else:
            pass
guess()
