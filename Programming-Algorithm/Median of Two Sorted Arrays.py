# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 11:36:45 2015

@author: ZSHU
"""
"""
pay attention to border conditioins
"""

class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):

        p1, p2, res=0,0,[]
        median=(len(nums1)+len(nums2))/2
        
        while len(res)<=median:
            if p1<=len(nums1)-1 and p2<=len(nums2)-1 and nums1[p1]<nums2[p2]:
                res.append(nums1[p1])
                p1+=1
            elif  p1<=len(nums1)-1 and p2<=len(nums2)-1 and nums1[p1]>nums2[p2]:
                res.append(nums2[p2])
                p2+=1
            else:
                if len(nums1)==0 or (p1==len(nums1) and nums1[p1-1]<nums2[p2]):
                    res.append(nums2[p2])
                    p2+=1
                elif len(nums2)==0 or (p2==len(nums2) and nums2[p2-1]<nums1[p1]):
                    res.append(nums1[p1])
                    p1+=1
                elif nums1[p1]==nums2[p2]:
                    res.append(nums1[p1])
                    res.append(nums2[p2])
                    if p1<=len(nums1)-1:
                        p1+=1
                    if p2<=len(nums2)-1:
                        p2+=1
        if (len(nums1)+len(nums2))%2==1:
            return res[median]
        else:
            return float((res[median]+res[median-1])/float(2))