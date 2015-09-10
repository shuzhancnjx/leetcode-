# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 11:45:02 2015

@author: ZSHU
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a=a[::-1]; b=b[::-1]
        i,j,carrier,res=0,0,0,''
        while i<len(a) and j<len(b):
            temp=int(a[i])+int(b[i])+carrier
            carrier=temp/2
            res+=str(temp%2); i+=1; j+=1
     
        while i<len(a):
            temp=int(a[i])+carrier
            carrier=temp/2
            res+=str(temp%2)
            i+=1

        while j<len(b):
            temp=int(b[j])+carrier
            carrier=temp/2
            res+=str(temp%2)
            j+=1
        if carrier!=0: res+=str(carrier)
        return res[::-1]
