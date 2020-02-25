#!/usr/bin/env python3.8
def calculator(a,b,op):
    a = int(a)
    b = int(b)
    if op=="+":
        c = a + b
        print(c)
    if op =="-":
        c = a - b
    if op == "*":
        c = a * b
    if op == "/":
        c = a / b
    return c
def main():
    c = input("first integer number to operate on: ")
    e = input("the operator: ")
    d = input("second integer number to operate on: ")
    
    result = calculator(c,d,e)
    
    print(c,e,d,"=",result)

main()