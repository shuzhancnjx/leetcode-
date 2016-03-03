# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:59:48 2015

@author: ZSHU
"""

"""
time limit exceed
"""
class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        
        def permute(words):
            if len(words)==1:
                return words
            else:
                per=[]
                for i in range(len(words)):
                    per+=[words[i] + word for word in permute(words[:i]+words[i+1:])]
                return per
        
        res=[]
        dic={}
        combin=permute(words)
        width=len(combin[0])
        
        for word in combin:
            dic[word[0]]=dic.get(word[0],[])+[word]
        i=0
        while i<len(s):
            if s[i] in dic.keys() and s[i:i+width] in dic[s[i]]:
                res+=[i]
                i=i+width
            else:
                i+=1
        return res 

"""
time limit exceed
""" 
  dic={}
  width=len(words[0])
  for word in words:
      dic[word]=words.count(word)
      
  def findSubstring(dic,s,i):
      if sum(dic.values())==0:
          return True
      else:
          if dic.get(s[i:i+width],0)>0:
              dic[s[i:i+width]]-=1
              if findSubstring(dic,s,i+width):
                  dic[s[i:i+width]]+=1
                  return True
              dic[s[i:i+width]]+=1
          else:
              return False 
  
  res=[]
  i=0
  while i<len(s):
      if findSubstring(dic,s, i):
          print i
          res+=[i]
          i+=width
      else:
          i+=1
"""
this one works, no recursive. 
"""   

class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        if len(s)< len(words)*len(words[0]):
            return []
        else:
            dic={}
            width=len(words[0])
            for word in set(words):
                dic[word]=words.count(word)
               
            res=[]
            i=0
            while i<=len(s)-width*len(words):
                dic2={}
                for j in range(len(words)):
                    substring=s[i+j*width: i+(j+1)*width]
                    if substring not in dic:
                        break 
                    dic2[substring]=dic2.get(substring,0)+1
                    if dic2[substring]>dic[substring]:
                        break
                    
                if j==len(words)-1 and dic==dic2:
                    res+=[i]
                i+=1
            
            return res 
           
                    












































     
                