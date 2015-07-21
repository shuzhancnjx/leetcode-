# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 10:04:33 2015

@author: ZSHU
"""

"""
Word Search II, Leetcode, 
BY, Zhan Shu, shuzhancnjx@gmail.com
"""

board=[['o','a','a','n'],
       ['e','t','a','e'],
       ['i','h','k','r'],
       ['i','f','l','v']
       ]
words=['oath','eat','pea','hhha']

class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        
        def Match(i, j, k, s, board):
            if k==len(s):
                return True 
            else: 
                if i>=0 and i<len(board) and j>=0 and j<len(board[0]) and board[i][j]==s[k]:
                    board[i][j],tmp="#",board[i][j]
                    if Match(i+1, j, k+1, s, board) or Match(i-1, j, k+1, s, board)\
                           or Match(i, j-1, k+1, s, board) or Match(i, j+1, k+1, s, board):
                        board[i][j]=tmp
                        return True 
                    else:
                        board[i][j]=tmp
                        return False     
                else:
                    return False 
        
    
        result=[]
        lookup={}
        for word in words:
            if word not in lookup.get(word[0],[]):
                lookup[word[0]]=lookup.get(word[0],[])+[word]
        potential=lookup.keys()
           
         for i in range(len(board)):
              for j in range(len(board[0])):
                  if board[i][j]in potential:
                      for word in lookup[board[i][j]]:
                          if Match(i, j, 0, word, board):
                              result+=[word]
                              lookup[board[i][j]].remove(word)
                              if lookup[board[i][j]]==[]: 
                                  del lookup[board[i][j]]
                                  potential=lookup.keys()
       return result
        
 

                 
         
                
         

                 
                 
             