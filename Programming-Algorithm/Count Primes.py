# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:20:24 2015

@author: ZSHU
"""  
"""
TLEd
"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        prime=[True]*max(n,2)
        prime[0],prime[1]=False, False 
        starting=2
        while starting**2<n:
            if prime[starting]:
                temp=starting**2
                while temp<n:
                    prime[temp]=False
                    temp+=starting
                starting+=1
        return sum(prime)           


"""
second one from internet
"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        prime=[True]*max(n,2)
        prime[0],prime[1]=False, False 
        starting=2
        while starting**2<n:
            if prime[starting]:
                temp=starting**2
                while temp<n:
                    prime[temp]=False
                    temp+=starting
            starting+=1
        return sum(prime)
