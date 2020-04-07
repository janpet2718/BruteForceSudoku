import Board

import copy
import numpy as np

class Solver(object):
    
    def __init__(self, board, N=0):
        self.board = board
        self.N = N
        
    def solve(self):

        print('Solving level {0} board'.format(self.N))
        
        # Determine all possible values
        possibleSolutions = self.board.findPossible()

        # Iterate over board:
        # - Update board with all uniquely determined values
        # - Find the cell with fewest possibilities for testing (minSolution)
        # - Detect cells with no solution
        minSolution = [0,0,range(1,10)]
        for n in range(len(possibleSolutions)):
            nSol = len(possibleSolutions[n][2])
            if  nSol== 0:
                print('   Inconsistent board. No solution at element ({0},{1}).'.format(possibleSolutions[n][0],possibleSolutions[n][1]))
                return 'failed'
            elif nSol == 1:
                print('   Updating unique solution cell ({0},{1})'.format(possibleSolutions[n][0],possibleSolutions[n][1]))
                self.board.board[possibleSolutions[n][0],possibleSolutions[n][1]] = possibleSolutions[n][2][0]
            else:
                if nSol < len(minSolution[2]):
                    minSolution = possibleSolutions[n]

        p = self.board.getUnknowns()
        print('   Board has {0} non-unique unknowns'.format(p))
                    
        # Return solution if all values are found
        if p == 0:
            print('Solution found')
            self.board.prettyPrint()
            return 'solved'
                    
        # Iterate over possible values for test cell
        for n in range(len(minSolution[2])):
            print('Testing cell ({0},{1}) {2}/{3}: '.format(minSolution[0],minSolution[1],n+1,len(minSolution[2])))
            testSolution = minSolution[2][n]
            newSolver = Solver(copy.deepcopy(self.board), self.N+1)
            newSolver.board.board[minSolution[0],minSolution[1]] = testSolution
            result = newSolver.solve()
            if result=="solved":
                exit(0)
            elif ((result=='failed') and (n==(len(minSolution[2])-1))):
                #print('Test value failed')
                return result
        
    
