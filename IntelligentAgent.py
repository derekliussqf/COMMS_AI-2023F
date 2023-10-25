#Chen Liu CL4452
import random
from BaseAI import BaseAI
import math
import time

class IntelligentAgent(BaseAI):
    '''def getMove(self, grid):
            # Selects a random move and returns it
            moveset = grid.getAvailableMoves()
            print(str(moveset) + '\n')
            return random.choice(moveset)[0] if moveset else None
    '''
    
    def getMove(self, grid):
        time_start = time.time()
        moveset = grid.getAvailableMoves()
        print(moveset)
        move, heu,smth = self.Maximize(grid, -math.inf, math.inf , time_start)
        return move
        
    def Maximize(self, grid, alpha, beta,times):
        moves = []
        maxmove = None
        maxheu = -math.inf
        moves = grid.getAvailableMoves()
        now = time.time()
        timenow = now-times
        if not moves: #or timenow >= 0.18/100000:
            heunow = grid.getCellValueValue((3,3))
            #heunow = self.evaluate(grid)
            return 2, heunow
            
        for move,newgrid in moves:
                print('inmax' + str(move) + str(newgrid.map))
                _, heu,newalpha, newbeta = self.Minimize(newgrid, alpha, beta,times)
                alpha = newalpha
                beta = newbeta
                print('current heu in max is' + str(heu))
                if heu > maxheu:
                    maxmove, maxheu = move, heu
                if maxheu >= beta:
                    break
                if maxheu > alpha:
                    alpha = maxheu
        return maxmove, maxheu, alpha , beta

    def Minimize(self, grid, alpha, beta,times):
        moves = []
        minmove = None
        minheu = math.inf
        moves = grid.getAvailableMoves()
        now = time.time()
        timenow = now - times
        if not moves: #or timenow >= 0.18/100000:
            heunow = grid.getCellValueValue((3,3))
            #heunow = self.evaluate(grid)
            return 2, heunow        
            
        for move,newgrid in moves:
                print('inmin' + str(move) + str(newgrid.map))

                movenow, heu,newalpha,newbeta = self.Maximize(newgrid ,alpha, beta,times)
                alpha = newalpha
                beta = newbeta
                print('current heu in min is' + str(heu))
                if heu < minheu:
                    minmove, minheu = move, heu
                if minheu <= alpha:
                    break
                if minheu < beta:
                    beta = minheu
        return minmove, minheu, alpha, beta

    def evaluate(board,commonRatio=0.25):
            linearWeightedVal = 0
            invert = False
            weight = 1.
            malus = 0
            criticalTile = (-1,-1)
            for y in range(0,4):
                for x in range(0,4):
                    b_x = x
                    b_y = y
                    if invert:
                        b_x = 4 - 1 - x
                    #linearW
                    currVal=board.getCellValueValue(b_x,b_y)
                    if(currVal == 0 and criticalTile == (-1,-1)):
                        criticalTile = (b_x,b_y)
                    linearWeightedVal += currVal*weight
                    weight *= commonRatio
                invert = not invert
                
            linearWeightedVal2 = 0
            invert = False
            weight = 1.
            malus = 0
            criticalTile2 = (-1,-1)
            for x in range(0,4):
                for y in range(0,4):
                    b_x = x
                    b_y = y
                    if invert:
                        b_y = 4 - 1 - y
                    #linearW
                    currVal=board.getCellValue(b_x,b_y)
                    if(currVal == 0 and criticalTile2 == (-1,-1)):
                        criticalTile2 = (b_x,b_y)
                    linearWeightedVal2 += currVal*weight
                    weight *= commonRatio
                invert = not invert
                
            
            linearWeightedVal3 = 0
            invert = False
            weight = 1.
            malus = 0
            criticalTile3 = (-1,-1)
            for y in range(0,4):
                for x in range(0,4):
                    b_x = x
                    b_y = 4 - 1 - y
                    if invert:
                        b_x = 4 - 1 - x
                    #linearW
                    currVal=board.getCellValue(b_x,b_y)
                    if(currVal == 0 and criticalTile3 == (-1,-1)):
                        criticalTile3 = (b_x,b_y)
                    linearWeightedVal3 += currVal*weight
                    weight *= commonRatio
                invert = not invert
                
            linearWeightedVal4 = 0
            invert = False
            weight = 1.
            malus = 0
            criticalTile4 = (-1,-1)
            for x in range(0,4):
                for y in range(0,4):
                    b_x = 4 - 1 - x
                    b_y = y
                    if invert:
                        b_y = 4 - 1 - y
                    #linearW
                    currVal=board.getCellValue(b_x,b_y)
                    if(currVal == 0 and criticalTile4 == (-1,-1)):
                        criticalTile4 = (b_x,b_y)
                    linearWeightedVal4 += currVal*weight
                    weight *= commonRatio
                invert = not invert
                
                
            linearWeightedVal5 = 0
            invert = True
            weight = 1.
            malus = 0
            criticalTile5 = (-1,-1)
            for y in range(0,4):
                for x in range(0,4):
                    b_x = x
                    b_y = y
                    if invert:
                        b_x = 4 - 1 - x
                    #linearW
                    currVal=board.getCellValue(b_x,b_y)
                    if(currVal == 0 and criticalTile5 == (-1,-1)):
                        criticalTile5 = (b_x,b_y)
                    linearWeightedVal5 += currVal*weight
                    weight *= commonRatio
                invert = not invert
                
            linearWeightedVal6 = 0
            invert = True
            weight = 1.
            malus = 0
            criticalTile6 = (-1,-1)
            for x in range(0,4):
                for y in range(0,4):
                    b_x = x
                    b_y = y
                    if invert:
                        b_y = 4 - 1 - y
                    #linearW
                    currVal=board.getCellValue(b_x,b_y)
                    if(currVal == 0 and criticalTile6 == (-1,-1)):
                        criticalTile6 = (b_x,b_y)
                    linearWeightedVal6 += currVal*weight
                    weight *= commonRatio
                invert = not invert
                
            
            linearWeightedVal7 = 0
            invert = True
            weight = 1.
            malus = 0
            criticalTile7 = (-1,-1)
            for y in range(0,4):
                for x in range(0,4):
                    b_x = x
                    b_y = 4 - 1 - y
                    if invert:
                        b_x = 4 - 1 - x
                    #linearW
                    currVal=board.getCellValue(b_x,b_y)
                    if(currVal == 0 and criticalTile7 == (-1,-1)):
                        criticalTile7 = (b_x,b_y)
                    linearWeightedVal7 += currVal*weight
                    weight *= commonRatio
                invert = not invert
                
            linearWeightedVal8 = 0
            invert = True
            weight = 1.
            malus = 0
            criticalTile8 = (-1,-1)
            for x in range(0,4):
                for y in range(0,4):
                    b_x = 4 - 1 - x
                    b_y = y
                    if invert:
                        b_y = 4 - 1 - y
                    #linearW
                    currVal=board.getCellValue(b_x,b_y)
                    if(currVal == 0 and criticalTile8 == (-1,-1)):
                        criticalTile8 = (b_x,b_y)
                    linearWeightedVal8 += currVal*weight
                    weight *= commonRatio
                invert = not invert
                
            maxVal = max(linearWeightedVal,linearWeightedVal2,linearWeightedVal3,linearWeightedVal4,linearWeightedVal5,linearWeightedVal6,linearWeightedVal7,linearWeightedVal8)
            if(linearWeightedVal2 > linearWeightedVal):
                linearWeightedVal = linearWeightedVal2
                criticalTile = criticalTile2
            if(linearWeightedVal3 > linearWeightedVal):
                linearWeightedVal = linearWeightedVal3
                criticalTile = criticalTile3
            if(linearWeightedVal4 > linearWeightedVal):
                linearWeightedVal = linearWeightedVal4
                criticalTile = criticalTile4
            if(linearWeightedVal5 > linearWeightedVal):
                linearWeightedVal = linearWeightedVal5
                criticalTile = criticalTile5
            if(linearWeightedVal6 > linearWeightedVal):
                linearWeightedVal = linearWeightedVal6
                criticalTile = criticalTile6
            if(linearWeightedVal7 > linearWeightedVal):
                linearWeightedVal = linearWeightedVal7
                criticalTile = criticalTile7
            if(linearWeightedVal8 > linearWeightedVal):
                linearWeightedVal = linearWeightedVal8
                criticalTile = criticalTile8
            
            return maxVal,criticalTile