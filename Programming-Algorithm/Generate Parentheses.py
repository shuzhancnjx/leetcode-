# -*- coding: utf-8 -*-
"""
Created on Tue Sep 01 12:19:47 2015

@author: ZSHU
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        def generate(starting, left, right):
            if left==target and right==target:
                res.append(starting)
                return
            elif left>target or right>target:
                return 
            else:
                if left==right: generate(starting+'(', left+1, right)
                elif left>right: 
                    generate(starting+')', left, right+1)
                    generate(starting+'(', left+1, right)
        res, target=[],n
        generate('(',1,0)
        return res 
        