# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:08:57 2015

@author: ZSHU
"""

'''
1. the basic idea is to have a list 'temp' formed by each letter in the string, i.e., list(s)
2. combine the components of 'temp' when they are palindrome
3. 'pos' is used to record the center for determing the palindrome
'''


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def par(res, temp, pos):
            if pos>len(temp)-1:
                res.append(temp)
                return 
            else:
                p1=pos-1; p2=pos+1
                while p1>=0 and p2<len(temp):
                    if temp[p1]==temp[p2]:
                        par(res, temp[:p1]+[''.join(temp[p1:p2+1])] +temp[p2+1:],p1+1)
                        p1-=1;p2+=1
                    else:
                        break 
             
                p1=pos; p2=pos+1
                while p1>=0 and p2<len(temp):
                    if temp[p1]==temp[p2]:
                        par(res, temp[:p1]+[''.join(temp[p1:p2+1])] +temp[p2+1:], p1+1)
                        p1-=1; p2+=1
                    else: 
                        break 
                par(res, temp,pos+1) # if no palindrome ceterned at temp[pos], then move on to next 
        res=[]
        par(res, list(s),0)
        return res 
         