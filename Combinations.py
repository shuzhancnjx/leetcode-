# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 15:17:40 2015

@author: ZSHU
"""

'''
typical recursive algorithm
'''


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        def combine(length, vector, temp, res):
            if len(temp)==length:
                res.append(temp)
                return 
            elif len(vector)==0:
                return 
            else:
                for i in range(len(vector)):
                    combine(length, vector[i+1:], temp+[vector[i]], res)
                    
        res=[]; vector=range(1, n+1)
        combine(k, vector, [], res )
        return res 

              