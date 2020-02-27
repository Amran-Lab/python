#!/usr/bin/env python3.8

class map_class:
    def __init__(self):
        row = [0,1,2,3,4,5]
        col = [0,1,2,3,4,5]
        for i in row:
            for j in col:
                self.board.append((i,j))
    def ship_destroyed(self,ship_lst):
        
        if len(ship_lst) == 0:
            print("you have destroyed a ship")
    def shoot(self,hit):
        x = 9
        y = 8
        if hit in self.ship_1:
            self.ship_1.remove(hit)
            self.board[self.board.index(hit)]=(x,x)
            print('you hit a ship')
        elif hit in self.ship_2:
            self.ship_2.remove(hit)
            self.board[self.board.index(hit)]=(x,x)
            print('you hit a ship')
        elif hit in self.ship_3:
            self.ship_3.remove(hit)
            self.board[self.board.index(hit)]=(x,x)
            print('you hit a ship')
        elif hit in self.ship_4:
            self.ship_4.remove(hit)
            self.board[self.board.index(hit)]=(x,x)
            print('you hit a ship')
        elif hit in self.board:           
            self.board[self.board.index(hit)]=(y,y)
            print('you hit nothing')
        else:
            print('not on the board')
        self.ship_destroyed(self.ship_1)
        self.ship_destroyed(self.ship_2)
        self.ship_destroyed(self.ship_3)
        self.ship_destroyed(self.ship_4)
    
            

            


    board = []
    ship_1 = [(2,0), (2,1), (2,2), (2,3)]
    ship_2 = [(4,0), (4,1), (4,2)]
    ship_3 = [(4,3), (5,3)]
    ship_4 = [(3,3), (3,4), (3,5)]
