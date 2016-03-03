# -*- coding: utf-8 -*-
"""
Created on Tue Sep 08 11:36:32 2015

@author: ZSHU
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dictionary={}
        
        for st in strs:
            label=''.join(sorted(st))
            dictionary[label]=sorted (dictionary.get(label,[])+[st])
        
        return dictionary.values()