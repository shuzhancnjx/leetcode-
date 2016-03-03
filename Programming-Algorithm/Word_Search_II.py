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

"""
Trie based algorithm, thanks the comments from: 
    http://bookshadow.com/weblog/2015/05/19/leetcode-word-search-ii/
"""       
 

class TrieNode:
    def __init__(self):
        self.childs=dict()
        self.isWord=False 

class Trie:
    def __init__(self):
        self.root=TrieNode()
        
    def addword(self, word):
        node=self.root
        for letter in word:
            child=node.childs.get(letter)
            if child==None:
                child=TrieNode()
                node.childs[letter]=child
            node=child
        node.isWord=True 
    
    def deleteword(self, word):
        node=self.root 
        temp=[]
        for letter in word: 
            temp.append((letter, node))
            child=node.childs.get(letter)
            if child==None:
                return
            node=child
            
        if node.isWord==False:
            return  
        if len(node.childs)>0:
            node.isWord=False
        else: 
            for letter, node in reversed(temp):
                del node.childs[letter]
                if len(node.childs)>0 or node.isWord:
                    break 
        return 

      
def findWords(board, words):

    
    def match(i,j,node,word, res):
        child=node.childs.get(board[i][j])
        if child==None:
            return 
            
        if child.isWord:
            res+=[word]
            trie.deleteword(word) 
            
        visited[i][j]=True 
        for cx, cy in change:
            x=i+cx
            y=j+cy
            if x<len(board) and x>=0 and y<len(board[0]) and y>=0 and not visited[x][y]: 
               match(x, y, child, word+board[x][y], res)
        visited[i][j]=False 
        
    trie=Trie()
    for word in words:
        trie.addword(word)
        
    visited=[[False for i in xrange(len(board[0]))] for j in xrange(len(board))]
    change=zip([1,0,-1,0],[0,1,0,-1])
    res=[]
    
   for i in range(len(board)):
        for j in range(len(board[0])):
            match(i,j,trie.root, board[i][j], res)
   return sorted(res)               
         
                
         

                 
                 
             