# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 15:04:50 2015

@author: ZSHU
"""

board=[['.' for i in range(9)] for i in range(9)]
board[0][0]='5'
board[0][1]='3'
board[0][4]='7'
board[1][0]='6'
board[1][3]='1'
board[1][4]='9'
board[1][5]='5'
board[2][1]='9'
board[2][2]='8'
board[2][7]='6'
board[3][0]='8'
board[3][4]='6'
board[3][8]='3'
board[4][0]='4'
board[4][3]='8'
board[4][5]='3'
board[4][8]='1'
board[5][0]='7'
board[5][4]='2'
board[5][8]='6'
board[6][1]='6'
board[6][6]='2'
board[6][7]='8'
board[7][3]='4'
board[7][4]='1'
board[7][5]='9'
board[7][8]='5'
board[8][4]='8'
board[8][7]='7'
board[8][8]='9'


class solution:
    
    def isvalid(number, i, j, board):
        board[i][j]='.'
        for k in range(len(board)):
            if number==board[k][j] or number==board[i][k]:
                return False 
        for k in range((i/3)*3, (i/3)*3+3):
            for f in range((j/3)*3, (j/3)*3+3):
                if number==board[k][f]:
                    return False 
        board[i][j]=number
        return True  
        
    def sudoku(board):
    
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j]=='.':
                    for number in '123456789':
                        board[i][j]=number
                        if isvalid(number, i, j, board) and sudoku(board):
                            return True 
                        else:
                            board[i][j]='.'
                    return False
        return True    
                        

sudoku(board)                      
                            
                            
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
        