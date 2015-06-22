# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 09:40:38 2015

@author: ZSHU
"""

# this one is similar to Sudoku

class Solution:
    
    def isvalid(depth, j, board):

        for k in range(depth):
            if board[k][j]=='Q':
                return False
            if j-k>=0 and board[depth-k][j-k]=="Q":
                return False 
            if j+k<=len(board)-1 and board[depth-k][j+k]=="Q":
                return False 
        return True 
        
    def Nqueen(self, n):
         def nqueenI(depth,board):
            if depth==n:
               result.append([''.join(tem) for tem in board])
               return 
            else: 
                for j in range(n):
                    board[depth]=['.' for i in range(n)]
                    if isvalid(depth, j, board):
                        board[depth][j]='Q'
                        nqueenI(depth+1, board)
         result=[]
         board=[['.' for i in range(n)] for i in range(n)]             
         nqueenI(0,board)
         return result

Solution().Nqueen(4)



### a different way of printing 
        board=[['.' for i in range(n)] for i in range(n)]
        def nqueen(depth,board):
            if depth==n:
                return [[''.join(tem) for tem in board]] 
            else:
                result=[]
                for j in range(n):
                    board[depth]=['.' for i in range(n)]
                    if isvalid(depth, j, board):
                        board[depth][j]='Q'
                        for temp in nqueen(depth+1, board):
                            if len(temp)==n:
                                result.append(temp)     
                return result
