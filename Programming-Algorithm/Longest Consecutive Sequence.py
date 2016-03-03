# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 10:40:59 2015

@author: ZSHU
"""
"""
i have the first one, time limit exceeds
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def link(number, dic, res, visited):
            if dic[number]==[]:
                return 
            if len(visited)==len(dic):
                return 
            else:
                for num in dic[number]:
                    if num not in visited:
                        visited.add(num)
                        res+=[num]
                        link(num, dic, res, visited)
        
        
        dic={}
        
        for number in nums:
            dic[number]=dic.get(number,[])
            if dic.get(number+1,None)!=None:
                dic[number+1]+=[number]
                dic[number]+=[number+1]
            if dic.get(number-1,None)!=None:
                dic[number-1]+=[number]
                dic[number]+=[number-1] 
        
        
        visited=set()
        length=0
        for number in nums:
            if number not in visited:
                visited.add(number)
                res=[number]
                link(number, dic, res, visited)
                length=max(length, len(res))
        return length

"""
the second one passes the tests
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=1
        
        while len(nums)>0:
            number=nums[0]
            nums.remove(number)
            start=1
        
            i=number
            while i+1 in nums:
                i=i+1
                nums.remove(i)
                start+=1
        
            i=number
            while i-1 in nums:
                i=i-1
                nums.remove(i)
                start+=1
            length=max(length, start)
        
        return length