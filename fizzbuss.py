#!/usr/bin/env python3.8
def fizzbuzz(b):
    for i in range(1,b+1):
        if i%5==0 and i%3==0:
            print("FizzBuzz", i)
        elif i%3==0:
            print("Fizz", i)
        elif i%5==0:
            print('Buzz', i)
        else:
            pass
#fizzbuzz(30)
def fizz(b):
    for i in range(1,b+1):
        strn = ''
        if i%3==0:
            strn+='Fizz'
        if i%5==0:
            strn+='Buzz'
        if len(strn)>=1:
            print(strn, i)
        strn=''
fizz(30)
