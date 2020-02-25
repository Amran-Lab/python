#!/usr/bin/env python3.8

numbers = ['0','1','2','3','4','5','6','7','8','9']

def create_number(phone_list):
    #phone_str = '('+str(phone_list[0])+str(phone_list[1])+str(phone_list[2])+')' + " " 
    #phone_str = str(phone_str)
    phone_str = '('
    for i in range(len(phone_list)):
        if i < 3:
            phone_str += str(phone_list[i])
        elif i == 3:
            phone_str += ') '+ str(phone_list[i])
        elif i>=3 and  i <6:
            phone_str += str(phone_list[i])
        elif i == 6:
            phone_str += " "+ str(phone_list[i])
        else:
            phone_str += str(phone_list[i])


    

    return phone_str


print(create_number([6,8,3,9,5,5,5,8,9,0]))