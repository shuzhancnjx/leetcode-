# -*- coding: utf-8 -*-
"""
Created on Tue Sep 01 11:19:47 2015

@author: ZSHU
"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        table={1:'I',4: 'IV', 5:'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90:'XC', 100: 'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}
        
        res=[]
        
        for prime in [10, 100, 1000, 10000]:
            digit=num%prime
            num=num-digit
            if table.get(digit,None)!=None:
                res.insert(0, table[digit])
            else:
                res.insert(0, table.get(prime/2,'')*(digit/(prime/2))+ table[prime/10]*((digit%(prime/2))/(prime/10)))
        
        return ''.join(res)
                