# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 14:03:28 2015

@author: ZSHU
"""

class Solution:
    # @param {string} beginWord
    # @param {string} endWord
    # @param {set<string>} wordDict
    # @return {integer}
    def ladderLength(self, beginWord, endWord, wordDict):
        
        def builddic(start,leng, end, dictionary):
            current, previous,loop,length=set(),set([start]),False,len(start)
            if start in dictionary: 
                dictionary.remove(start)
            while loop==False:
                for word in previous:
                    
                    for i in range(length): 
                        for letter in 'abcdefghijklmnopqrstuvwxyz':
                            if letter!=word[i]:
                                newword=word[:i]+letter+word[i+1:]
                                if newword in dictionary or newword==end:
                                     if newword!=end: 
                                         current.add(newword)
                                     else:
                                         loop=True
           
                if len(current)==0 or loop==True:
                    break
                else:
                    dictionary=dictionary.difference(current)
                    leng[0]+=1
                    previous=current
                    current=set()
            return loop
        
        leng=[0]
        if builddic(beginWord,leng, endWord,wordDict):
            return leng[0]+2
        return leng[0]
            
    