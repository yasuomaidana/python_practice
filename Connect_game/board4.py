import numpy as np

class Board():
    game_over = False
    def __init__(self,row=6,col=7):
        if row<4 or col <4:
            print("Your settings were wrong")
            print("We design a board of 6 rows and 7 columns")
            row=6
            col=7
        self.ROW_COUNT=row
        self.COLUMN_COUNT=col
        self.board=np.zeros((row,col))
    def drop_piece(self,row,col,piece):
        self.board[row,col]=piece
    def fill(self,col,piece):
        i=0
        for row in self.board: 
            if row[col] == 0:
                self.board[i][col]=piece
                break
            i+=1 
    def is_valid_location(self,col,piece):
        if self.board[self.ROW_COUNT-1][col]==0:
            self.fill(col,piece)
            return True
        return False
    def checkWin(self,player):
        sX=self.ROW_COUNT-3
        sY=self.COLUMN_COUNT-3
        plB = np.where(self.board==player,1,0)
        for i in range(sX):
            for j in range(sY):
                t_plB=plB[i:i+4,j:j+4]
                c_R=t_plB.sum(0)
                c_C=t_plB.sum(1)
                c_DR=t_plB.diagonal().sum()
                c_DL=t_plB[:,::-1].diagonal().sum()
                if 4 in c_R or 4 in c_C or c_DR==4 or c_DL==4:
                    self.game_over = True
                    break
            if self.game_over:
                break
        
    def __str__(self):
        print(np.flip(self.board,0))
        return ""