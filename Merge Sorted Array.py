# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 16:09:17 2015

@author: ZSHU
"""

'''
starting from the end, not the beginning for the list structure
'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i,j,point=m-1,n-1, m+n-1
        while i>=0 and j>=0:
            if nums1[i]>=nums2[j]:
                nums1[point]=nums1[i]; i-=1
            elif nums1[i]<nums2[j]:
                nums1[point]=nums2[j]; j-=1
            point-=1

        if j>=0:
            nums1[:j+1]=nums2[:j+1]
        
    