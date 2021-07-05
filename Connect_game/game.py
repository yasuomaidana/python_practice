from board4 import Board
import pygame
import sys
import math
import copy
class winGame(Board):
    turn = 1
    color_case=(0,0,255)
    color_case_hole=(0,0,0)
    color_player1=(255,0,0)
    color_player2=(0,255,0)
    colorP=[color_player1,color_player2]
    posX=0
    
    def __init__(self,rows,cols,square):
        Board.__init__(self,rows,cols)
        self.width = cols*square
        self.height = (rows+1)*square
        self.size = (self.width,self.height)
        self.SQUARESIZE = square
        self.offset=int(self.SQUARESIZE/2)
        self.RADIUS=int(self.SQUARESIZE/2-self.SQUARESIZE*0.05)
        self.screen = pygame.display.set_mode(self.size)
        self.draw_board()
        
        self.font = pygame.font.SysFont("monospace",75)
    def colTurn(self):
        if self.is_valid_location(self.col,self.turn):
            self.draw_board()
            self.checkWin(self.turn)
            if self.game_over:
                oM=copy.copy(self.turn)
                self.turn+=1
                if self.turn>2:
                    self.turn=1
                self.drawMove()
                label = self.font.render("Player {} won!!!".format(oM),
                1,self.colorP[oM-1])
                self.screen.blit(label,(40,10))
                pygame.display.update()
                return None
            self.turn+=1
        if self.turn>2:
            self.turn=1
    def draw_PlayerC(self):
        offset=self.offset
        for c in range(self.COLUMN_COUNT):
            for r in range(self.ROW_COUNT):
                if self.board[r][c]==1:
                    pygame.draw.circle(self.screen,self.color_player1,
                        (c*self.SQUARESIZE+offset,#x
                        self.height-int((r)*self.SQUARESIZE+offset))#y
                    ,self.RADIUS)
                elif self.board[r][c]==2:
                    pygame.draw.circle(self.screen,self.color_player2,
                        (c*self.SQUARESIZE+offset,#x
                        self.height-int((r)*self.SQUARESIZE+offset))#y
                    ,self.RADIUS)
    def draw_board(self):
        offset=self.offset
        for c in range(self.COLUMN_COUNT):
            for r in range(self.ROW_COUNT):
                pygame.draw.rect(self.screen,self.color_case,
                (c*self.SQUARESIZE,(r+1)*self.SQUARESIZE,self.SQUARESIZE,self.SQUARESIZE))
                
                pygame.draw.circle(self.screen,self.color_case_hole,
                    (c*self.SQUARESIZE+offset,#x
                    (r+1)*self.SQUARESIZE+offset)#y
                ,self.RADIUS)
        self.draw_PlayerC()
        pygame.display.update()
        self.drawMove()
    def getCol(self,event):
        self.posX=event.pos[0]
        self.col=int(math.floor(self.posX/self.SQUARESIZE))
        self.drawMove()
    def drawMove(self):
        posX=self.posX
        pygame.draw.rect(self.screen,self.color_case_hole,(0,0,self.width,self.SQUARESIZE))
        color=self.colorP[self.turn-1]
        pygame.draw.circle(self.screen,color,(posX,int(self.SQUARESIZE/2)),self.RADIUS)
        pygame.display.update()
ROW_COUNT = 6
COLUMN_COUNT= 7
SQUARESIZE=100
pygame.init()
wGame = winGame(ROW_COUNT,COLUMN_COUNT,SQUARESIZE)

while not wGame.game_over:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            wGame.getCol(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            wGame.colTurn()
    if wGame.game_over:
        pygame.time.wait(3000)