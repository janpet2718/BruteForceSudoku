import numpy as np

class Board(object):
    def __init__(self, board=np.zeros([9,9], dtype=np.int)):
        self.board = board


    def getRow(self, i):
        return self.board[i,:]

    def getCol(self, j):
        return self.board[:,j]

    def getCell(self, i, j):
        return np.ravel(self.board[np.min(self.getCellRange(i)):np.max(self.getCellRange(i))+1, np.min(self.getCellRange(j)):np.max(self.getCellRange(j))+1 ])


    def getCellRange(self, k):
        if k<3:
            return range(0,3)
        elif k>5:
            return range(6,9)
        else:
            return range(3,6)

    def getUnknowns(self):
        n = 0
        for i in range(0,9):
            for j in range(0,9):
                if self.board[i,j]==0:
                    n += 1
        return n
        
    def findPossible(self):
        possibleValues = list()
        for i in range(0,9):
            for j in range(0,9):
                if self.board[i,j] == 0:
                    vals = range(1,10)
                    row  = self.getRow(i)
                    col  = self.getCol(j)
                    cell = self.getCell(i,j)
                    for hasVal in np.hstack([row,col,cell]):
                        try:
                            vals.remove(hasVal)
                        except ValueError:
                            pass
                    #if len(vals)==0:
                        #print('      Inconsistent board. No solution at element ({0},{1}).'.format(i,j))
                    #self.prettyPrint()
                    #exit(1)
                    possibleValues.append([i,j,vals])
        return possibleValues

    def prettyPrint(self):
        #print(self.board)
        print('|-----------------------|')
        for i in range(0,9,3):
            for ii in range(0,3):
                print('|'),
                for j in range(0,9,3):
                    for jj in range(0,3):
                        print('{0}'.format(self.board[i+ii,j+jj])),
                    print('|'),
                print('')
                              
            print('|-----------------------|')
