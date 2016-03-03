# -*- coding: utf-8 -*-
"""
Created on Wed Sep 09 09:52:52 2015

@author: ZSHU
"""

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums=range(1, n+1); pernum=1; res='';k-=1
        
        for number in xrange(1, n):
            pernum*=number
        
        while len(nums)>1:
            current=nums[k/pernum]
            res+=str(current)
            nums.remove(current)
            k=k%pernum; n-=1; pernum/=n
        res+=str(nums[0])
        return res 
            