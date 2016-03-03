# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 12:57:15 2015

@author: ZSHU
"""
"""
detailed explanation from this link: 
http://yucoding.blogspot.com/2015/06/leetcode-question-bitwise-and-of.html
"""
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        """
        thanks the explanation from the link: http://yucoding.blogspot.com/2015/06/leetcode-question-bitwise-and-of.html
        """
        
        p=0
        while m!=n: 
            m=m>>1
            n=n>>1
            p+=1
        return m<<p 