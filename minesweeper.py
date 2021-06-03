import random
import re

class Game:
    def __init__(self,dim_size,num_bombs):
        self.dim_size=dim_size
        self.num_bombs=num_bombs
        
        self.board=self.make_new_board()
        self.assign_values_to_board()
        
        self.dug=set()


    def make_new_board(self):
        board=[[None for i in range(self.dim_size)] for i in range(self.dim_size)]
        bombs_planted=0

        while (bombs_planted<self.num_bombs):
            loc=random.randint(0,(self.dim_size**2) -1 )
            row=loc//self.dim_size
            col=loc%self.dim_size

            if(board[row][col] == '*'):
                continue
            board[row][col]='*'
            bombs_planted+=1

        return board

    def assign_values_to_board(self):

        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c]=='*':
                    continue
                self.board[r][c]=self.get_num_neighbouring_bombs(r,c)

    def get_num_neighbouring_bombs(self,row,col):
        num_neighbouring_bombs=0
        for i in range(max(0,row-1),min(self.dim_size-1,row+1)+1):
            for j in range(max(0,col-1),min(self.dim_size-1,col+1)+1):
                if(i==row and j==col):
                    continue
                if(self.board[i][j]=='*'):
                    num_neighbouring_bombs+=1
        return num_neighbouring_bombs

    def dig(self,row,col):
        self.dug.add((row,col))
        if(self.board[row][col]=='*'):
            return False
        elif self.board[row][col]>0:
            return True
        
        for i in range(max(0,row-1),min(self.dim_size-1,row+1)+1):
            for j in range(max(0,col-1),min(self.dim_size-1,col+1)+1):
                if (i,j) in self.dug:
                    continue
                self.dig(i,j)

        return True

    def display_board(self):
        for r in range(self.dim_size):
            arr=[]
            for c in range(self.dim_size):
                if (r,c) in self.dug:
                    arr+=[str(self.board[r][c])]
                else:
                    arr+=[' ']
            row=['|','|'.join(arr),'|']
            # print('|'.join(arr))
            print(''.join(row))



def play(dim_size=4,num_bombs=4):
    game=Game(dim_size,num_bombs)
    safe=True

    while len(game.dug)<game.dim_size**2 - num_bombs:
        game.display_board()
        user_input=re.split(',(\\s)*',input("Specify the location to dig"))
        r=int(user_input[0])
        c=int(user_input[-1])
        print(r,c)
        if(r<0 or r>=game.dim_size or c<0 or c>=game.dim_size):
            print("Invalid location, enter input again")
            continue

        safe=game.dig(r,c)
        if not safe:
            print("You have dug a bomb, YOU HAVE LOST!")
            # game.dug.add((r,c) for r in range(game.dim_size) for c in range(game.dim_size))
            # game.dug=[(r,c) for r in range(game.dim_size) for c in range(game.dim_size)]
            game.dug=set((r,c) for r in range(game.dim_size) for c in range(game.dim_size))
            game.display_board()
            # print(game.board)
            return
    
    print("CONGRATULATIONS, YOU HAVE WON!") 

if __name__=='__main__':
    play()
