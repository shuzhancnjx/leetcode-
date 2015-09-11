# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 09:37:34 2015

@author: ZSHU
"""

'''
binary search: two levels 
'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        left=0; right=len(matrix)-1

        while right>left:
            if target >=matrix[left][0] and target<=matrix[left][-1]:
                right=left
            elif target >=matrix[right][0] and target<=matrix[right][-1]:
                left=right
            else:
                center=(left+right)/2
                if target >=matrix[center][0] and target<=matrix[center][-1]:
                    left=center; right=center
                elif target>matrix[center][-1]:
                    left=center+1
                else:
                    right=center-1
                    
        temp=matrix[left]; left=0; right=len(temp)-1

        while right>=left:
            if temp[left]==target:
                return True 
            elif temp[right]==target:
                return True 
            else:
                center=(left+right)/2
                if temp[center]==target:
                    return True 
                else:
                    if temp[center]>target:
                        right=center-1
                        left+=1
                    elif temp[center]<target:
                        left=center+1
                        right-=1
        return False                
            
    

    
    