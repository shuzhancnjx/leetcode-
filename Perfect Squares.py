# -*- coding: utf-8 -*-
"""
Created on Fri Oct 02 14:12:06 2015

@author: ZSHU
"""

"""
https://leetcode.com/discuss/56982/o-sqrt-n-in-ruby-and-c
"""
 class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n%4==0:
            n/=4
        if n%8==7:
            return 4
        
        for i in xrange(0,n+1):
            temp=i*i
            if temp<=n:
                if int((n-temp)**(0.5))**2+temp==n: 
                    return 1+ (0 if temp==0 else 1)
            else:
                break 
            
        return 3

"""
TLEd
"""

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        def combine(nums, n, temp, res):
            if temp>4 or temp>=res[0]:
                return 
            elif n==0:
                res[0]=min(res[0], temp)
                return 
            else:
                 if n in nums:
                     combine(nums, 0, temp+1, res)
                 else:
                     for i in range(len(nums)):
                         if n>nums[i]: combine(nums[i:], n-nums[i], temp+1, res)
                   
        
        nums=[]
        for i in xrange(1,n+1):
            if i**2<n:
                nums.insert(0, i**2)
            elif i**2==n:
                return 1
            else:
                break   
            
        res=[2**31]
        combine(nums, n, 0, res)
        return res[0]