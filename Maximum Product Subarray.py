# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 09:33:50 2015

@author: ZSHU
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def maxvalue(nums):
            if len(nums)==0: return
            elif len(nums)==1: return nums[0]
            else:
                stack=[nums[0]];value=nums[0]; negative=None if nums[0]>0 else nums[0]
                for number in nums[1:]:
                    stack.append(stack[-1]*number)
                    if stack[-1]>0:
                        value=max(value, stack[-1])
                    if stack[-1]<0 and negative==None:
                        negative=stack[-1]
                if stack[-1]<0: value=max(stack[-1]/negative, value)
                return value
                 
        if len(nums)==0:
            return 
        elif len(nums)==1:
            return nums[0]
        else:
            i=0; maximum=-2**31
            while i<=len(nums) and nums!=[]:
                if i<len(nums) and nums[i]!=0:
                    i+=1
                else:
                    maximum=max(maximum, maxvalue(nums[:i]),0)
                    nums=nums[i+1:]; i=0
            return maximum 
             

