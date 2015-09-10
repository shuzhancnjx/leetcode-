# -*- coding: utf-8 -*-
"""
Created on Wed Sep 09 15:27:57 2015

@author: ZSHU
"""


 class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        temp=digits[::-1]
        carrier, res=1, []
        for number in temp:
            tem=number+carrier
            carrier=tem/10
            res.append(tem%10)
        if carrier!=0:
            res.append(carrier)
        return res[::-1]   