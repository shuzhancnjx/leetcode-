# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:28:16 2015

@author: ZSHU
"""
"""
logically easy, just some concer cases
"""

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1=version1.split('.'); version2=version2.split('.')

        i=0
        while i<len(version1) and i<len(version2):
            if int(version1[i])>int(version2[i]):
                return 1
            elif int(version1[i])<int(version2[i]):
                return -1
            else:
                i+=1
        
        if len(version1)>len(version2):
            for letter in version1[i:]:
                if int(letter)>0:
                    return 1
            return 0
        elif len(version1)<len(version2):
            for letter in version2[i:]:
                if int(letter)>0:
                    return -1
            return 0
        else:
            if int(version1[len(version1)-1])>int(version2[len(version1)-1]): return 1
            elif int(version1[len(version1)-1])<int(version2[len(version1)-1]): return -1 
            else: return 0 
            
"""
the same logic as above, but a more simplified version 
"""
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1=version1.split('.'); version2=version2.split('.')
        l1=len(version1);l2=len(version2); i=0
        while i<l1 and i<l2:
            if int(version1[i])>int(version2[i]):
                return 1
            elif int(version1[i])<int(version2[i]):
                return -1
            i+=1
        
        if l1>l2:
            for letter in version1[i:]:
                if int(letter)>0:
                    return 1
      
        elif l1<l2:
            for letter in version2[i:]:
                if int(letter)>0:
                    return -1
        return 0
       
