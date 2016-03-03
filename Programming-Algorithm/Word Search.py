# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 10:21:09 2015

@author: ZSHU
"""

"""
an typical example of backtracking, with trimming condition
"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        def search(i, j, word, board):
            if len(word)==0:
                return True 
            elif i<0 or i>=len(board) or j<0 or j>=len(board[0]):
                return False 
            else:
                if board[i][j]==word[0]:
                    board[i][j], temp='.', board[i][j]
                    if search(i+1,j, word[1:], board) or\
                       search(i-1,j,word[1:], board) or\
                       search(i, j+1, word[1:],board) or\
                       search(i,j-1,word[1:],board):
                          return True
                    else:
                        board[i][j]=temp
                    return False 
                else:
                    return False 
        
        for i in range(len(board)):
            board[i]=list(board[i])
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if search(i,j,word,board):
                        return True 
        return False