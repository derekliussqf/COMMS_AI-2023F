#Chen Liu CL4452
import random
from BaseAI import BaseAI
import math
from datetime import datetime 
import statistics
import numpy as np

class IntelligentAgent(BaseAI):
    def getMove(self, grid):
        #out_filename = 'output.txt'
        #outfile = open(out_filename, "w")
        #outfile.write(str(grid.map))

        time_start = datetime.now() 
        hue , move = self.Maximize(grid, -math.inf, math.inf , time_start,3)
        return move
        
    def Maximize(self, grid, alpha, beta, times, depth):
        moves = grid.getAvailableMoves()

        if (not moves) or depth == 0 or (datetime.now() - times).seconds >= 0.20:
            #heu = self.evaluate(grid)
            heu = self.heuristic(grid,depth)
            return  heu, None

        best_move = None
        for move, newgrid in moves:
            val, _ = self.Minimize(newgrid, alpha, beta, times, depth - 1)
            if val > alpha:
                alpha = val
                best_move = move
            if alpha >= beta:
                break

        return alpha, best_move

    def Minimize(self, grid, alpha, beta, times, depth):
        
        if not grid.getAvailableMoves() or depth == 0 or (datetime.now() - times).seconds >= 0.20:
            #heu = self.evaluate(grid)
            heu = self.heuristic(grid,depth)
            return  heu, None
        
        best_val = math.inf
        blank = []
        for y in range(0, 4):
            for x in range(0, 4):
                if grid.getCellValue((x, y)) == 0:
                    blank.append((x, y))

        for block in blank:
            for tile_value in [2, 4]:
                new_grid = grid.clone()
                new_grid.setCellValue(block, tile_value)
                val, move = self.Maximize(new_grid, alpha, beta, times, depth - 1)
                if val < best_val:
                    best_val = val
                if val <= alpha:
                    break
                if val < beta:
                    beta = val

        return best_val, move

    def heuristic(self, grid,depth):
            
                
            mono = self.monotonicity(grid)*50
            smo = self.smoothness(grid)*0.5
            em = self.empty_cells(grid)*1024
            cb = self.edge_corner_bonus(grid)*0.1
            eve = self.evaluateSnake(grid)*0.005
                        
            check1024 = False
            check2048 = False
            for row in grid.map:
                if (1024 in row) :
                    check1024 = True
                    break
                if (2048 in row): 
                    check2048 = True
                    break
            if check1024:
              mono*=5
              smo*=5
              em *=2
              eve*= 0.5
            if check2048:
              mono*=5
              smo*=5
              em *=2
              eve*= 0.5
            heu  = mono + smo  + em + eve + cb 
            out_filename = 'output.txt'
            outfile = open(out_filename, "w")
            outfile.write('mono' + str(mono) + ' ' + 'smo' + str(smo) + ' ' +'em' + str(em) + ' ' + 'cb' + str(cb) + ' eve' + str(eve))
            return  heu
        
    def monotonicity(self,grid):
        results = [0, 0, 0, 0]
        for x in range(4):
            now = 0
            next = now+1
            while next < 4:
                while next < 4 and not grid.map[x][next]:
                    next += 1
                if next >= 4:
                    next -= 1
                nowValue = math.log(grid.map[x][now], 2) if grid.map[x][now] else 0
                nextValue = math.log(grid.map[x][next], 2) if grid.map[x][next] else 0
                if nowValue > nextValue:
                    results[0] += nextValue - nowValue
                elif nextValue > nowValue:
                    results[1] += nowValue - nextValue
                now = next
                next += 1
        for y in range(4):
            now = 0
            next = now+1
            while next < 4:
                while next < 4 and not grid.map[next][y]:
                    next += 1
                if next >= 4:
                    next -= 1
                nowValue = math.log(grid.map[now][y], 2) if grid.map[now][y] else 0
                nextValue = math.log(grid.map[next][y], 2) if grid.map[next][y] else 0
                if nowValue > nextValue:
                    results[2] += nextValue - nowValue
                elif nextValue > nowValue:
                    results[3] += nowValue - nextValue
                now = next
                next += 1
        return max(results[0], results[1]) + max(results[2], results[3])

    def smoothness(self ,grid):
        smoothness = 0
        for i in range(grid.size):
            for j in range(grid.size - 1):
                if grid.map[i][j] != 0:
                    k = j + 1
                    while k < grid.size and grid.map[i][k] == 0:
                        k += 1
                    if k < grid.size:
                        smoothness -= abs(grid.map[i][j] - grid.map[i][k])
        return smoothness

    def empty_cells(self ,grid):
        return len([(i, j) for i in range(grid.size) for j in range(grid.size) if grid.map[i][j] == 0])

    def edge_corner_bonus(self, grid):
        bonus = 0
        for i in range(1, 3):
            bonus += 2 * grid.getCellValue((0, i))
            bonus += 2 * grid.getCellValue((3, i))
            bonus += 2 * grid.getCellValue((i, 0))
            bonus += 2 * grid.getCellValue((i, 3))

        return bonus



    def evaluateSnake(self, grid):
        weight = 2
        snake_scores = []

        for direction in range(8):
            inv_x = direction % 2 == 1
            inv_y = direction // 2 == 1
            inv_coef = direction // 4 == 1

            score = 0
            coef = 0

            for y in range(4 - inv_y):
                for x in range(4 - inv_x):
                    in_x = x if not inv_x else 3 - x
                    in_y = y if not inv_y else 3 - y
                    score += grid.getCellValue((in_x, in_y)) * (weight ** coef)
                    coef += 1

            snake_scores.append(score)
        return max(snake_scores)