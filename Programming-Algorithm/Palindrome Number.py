# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 15:07:24 2015

@author: ZSHU
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x>=0 and x<10:
            return True 
        elif x<0 or x%10==0:
            return False 
      
        temp=1 
        while x/temp>=10:
            temp*=10
        
        while temp>1:
            if x/temp==x%10:
                x=(x%temp-x%10)/10
                temp/=100
            else:
                return False 
        return True 