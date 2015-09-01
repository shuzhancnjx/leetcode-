# -*- coding: utf-8 -*-
"""
Created on Tue Sep 01 11:32:21 2015

@author: ZSHU
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        table={'2':'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        def combine(s):
            if len(s)==1:
                return list(table[s])
            else:
                res=[]
                for letter in table[s[0]]:
                    res+=[letter +letter1 for letter1 in combine(s[1:])]
                return res 
        if len(digits)<1:
            return []
            
        return combine(digits)