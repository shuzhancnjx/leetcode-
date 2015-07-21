# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 08:58:04 2015

@author: ZSHU
"""
 
 ratings=[1,0,2]
 ratings=[3,4,5,1,3,6,7,6,3]

"""
thanks the comment from: http://www.cnblogs.com/zuoyuan/p/3760890.html
""" 
class Solution:
    # @param {integer[]} ratings
    # @return {integer}
    def candy(self, ratings):
        if len(ratings)==1: 
            return 1 
        else:
            nums=[1 for i in range(len(ratings))]
            for i in range(1, len(ratings)):
                if ratings[i]>ratings[i-1]:
                    nums[i]=nums[i-1]+1
            for i in range(len(ratings)-2, -1,-1):
                if ratings[i]>ratings[i+1]:
                    nums[i]= max(nums[i+1]+1,nums[i])
            return sum(nums)
