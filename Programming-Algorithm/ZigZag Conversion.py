# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 12:34:44 2015

@author: ZSHU
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s)<=numRows or numRows==1:
            return s
            
        res, length=['']*numRows, 2*(numRows-1)
        for i in range(len(s)):
            res[i%length if i%length<numRows else length-i%length]+=s[i]
        return ''.join(res)