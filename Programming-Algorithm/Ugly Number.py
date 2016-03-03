# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 16:57:20 2015

@author: ZSHU
"""

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==0:
            return False 
        if num==1:
            return True 
            
        prime=[2,3,5]
        while num not in prime:
            dp=[True, True, True]
            for i in range(len(prime)):
                if num%prime[i]==0:
                    num/=prime[i]
                    break
                else:
                    dp[i]=False
                    if not any(dp):
                        return False
        return True 