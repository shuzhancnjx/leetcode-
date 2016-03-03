# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 09:21:25 2015

@author: ZSHU
"""
'''
some small concer cases: 
a. when numerator is 0 
b. when numerator or denominator is negative 
c. recurring cases how to stop and proceed
'''


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """f
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator==0:
            return '0'
        
        sign=1
        if numerator<0: sign*=-1; numerator*=-1
        if denominator<0: sign*=-1; denominator*=-1
            
        first=str(numerator/denominator)
        numerator=numerator%denominator
        if numerator==0:
            return ('' if sign==1 else '-')+str(first)
        else:
            stack=[];res=''
            first=str(first)+"."
            while stack==[] or numerator not in stack:
                stack.append(numerator)
                res+=str((numerator*10)/denominator)
                numerator=(numerator*10)%denominator
                if numerator==0:
                    return ('' if sign==1 else '-')+first+res 
            for i in range(len(stack)):
                if stack[i]==numerator:
                    return ('' if sign==1 else '-')+ first+ res[:i]+"("+res[i:]+")"

"""
Improve the running speed by using HASP table
"""
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """f
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator==0:
            return '0'
        
        sign=1
        if numerator<0: sign*=-1; numerator*=-1
        if denominator<0: sign*=-1; denominator*=-1
        sign= '' if sign==1 else '-' 
        
        first=str(numerator/denominator)
        numerator=numerator%denominator
        
        if numerator==0:
            return sign+str(first)
        else:
            stack={};res='';first=str(first)+".";pos=0
            while stack.get(numerator,None)==None:
                stack[numerator]=pos;pos+=1
                res+=str((numerator*10)/denominator)
                numerator=(numerator*10)%denominator
                if numerator==0:
                    return sign+first+res
            pos=stack[numerator]
            return sign+ first+ res[:pos]+"("+res[pos:]+")"