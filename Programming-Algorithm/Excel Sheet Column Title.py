# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:47:23 2015

@author: ZSHU
"""

"""
Solution I: using chr and ord
"""
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res=''
        while n>0:
            if n%26==0:
                res='Z'+res
                n=n/26-1
            else:
                res= chr(ord('A')+n%26-1)+res
                n=n/26
           
        return res

"""
Solution II: a tedious one
"""
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        dic={}; letter='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(1,27):
            dic[i]=letter[i-1]       
        res=''
        while n>26:
            pos=0;sum=0
            while sum<n:
                sum+=26**(pos+1)
                pos+=1

            temp=n/(26**(pos-1)); tem=n%(26**(pos-1))
            if tem==0: res+=dic[temp-1]; n=26**(pos-1)
            else: res+=dic[temp]; n=tem
        return res+dic[n]