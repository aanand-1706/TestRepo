import pprint

class Sudoku:
    def find_next_empty(self,board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==-1:
                    return i,j
        
        return None,None

    def display(self,board):
        pprint.pprint(board)


    def is_valid(self,board,row,col,val):
        
        if val in board[row]:
            return False

        for i in range(len(board)):
            if board[i][col]==val:
                return False
        
        r=(row//3)*3
        c=(col//3)*3

        for i in range(r,r+3):
            for j in range(c,c+3):
                if board[i][j]==val:
                    return False

        return True

    def play(self,board):
        row,col=self.find_next_empty(board)
        if row==None:
            self.display(board)
            return True

        for val in range(1,10):
            if self.is_valid(board,row,col,val):
                board[row][col]=val
                if self.play(board):
                    return True
                board[row][col]=-1

        return False    
    


if __name__=='__main__':
    example_board=[
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    game=Sudoku()
    game.play(example_board)
    # display(example_board)