#!/usr/bin/env python3.8
from map import map_class
3,

new_map = map_class()


def create_board(board):
    lst = []
    for el in board:
        
        if el == (9,9):
            lst.append('1')
        elif el == (8,8):
            lst.append('x')
            
        else:
            lst.append('0')
    row1 = ' '.join(lst[:6])
    row2 = ' '.join(lst[6:12])
    row3 = ' '.join(lst[12:18])
    row4 = ' '.join(lst[18:24])
    row5 = ' '.join(lst[24:30])   
    row6 = ' '.join(lst[30:])   
    string = ("{0}\n{1}\n{2}\n{3}\n{4}\n{5}").format(row1,row2,row3,row4,row5,row6)
    print(string)
    return lst
"""new_map.shoot((2,3))
new_map.shoot((2,1))
new_map.shoot((2,4))"""
flag = True
create_board(new_map.board)
while flag:
    play = input('do you want to play y/n ')
    if play == 'y':
        
        while flag:
            x = input("pick row coordinate: ")
            y = input("pick column coordinate: ")
    
            new_map.shoot((int(x)-1,int(y)-1))
            lst = create_board(new_map.board)
            sunk = 0
            waste = 0
            if '0' not in lst:
                print('you have finished')
                flag = False
            else:
                pass
            for i in range(len(lst)):
                if lst[i] == '1':
                    sunk+=1
                elif lst[i]=='x':
                    waste+=1
                else:
                    pass
            if sunk == 12:
                print('you win')
                flag = False
            if waste ==10:
                print('YOU LOSE')
                flag = False

    elif play == 'n':
        flag = False
        
    else:
        pass
    
    

