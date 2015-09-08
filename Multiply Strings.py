# -*- coding: utf-8 -*-
"""
Created on Tue Sep 08 09:35:43 2015

@author: ZSHU
"""

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=='0' or num2=='0':
            return '0'
        
        num1=num1[::-1]; num2=num2[::-1]; num=0
        
        for i in range(len(num1)):
            multi=int(num1[i]);carrier=0;j=0;tem=''
            while j<len(num2):
                temp=int(num2[j])*multi+carrier
                tem+=str(temp%10)
                carrier=temp/10
                j+=1
            if carrier>0:
                num+=int(str(carrier)+tem[::-1])*(10**i)
            else:
                num+=int(tem[::-1])*(10**i)
        return str(num)
