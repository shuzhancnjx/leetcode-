# -*- coding: utf-8 -*-
"""
Created on Wed Sep 02 14:21:01 2015

@author: ZSHU
"""
"""
a lot of small cases: 
1. divisor==0 or dividend=0 
2. if res >= 2**31 or res <= 2**31
3. postive and negative signs 
"""



class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor==0: 
            return 0
        elif dividend==0:
            return 0
        elif abs(divisor)==1:
            temp=dividend if divisor>0 else -dividend 
            if temp>2**31:  
                return 2**31-1
            elif temp<-2**31:
                return -2**31+1
        
        res, upper, lower=0, abs(dividend), abs(divisor)
        while upper>=lower:
            temp, n=lower,1
            while temp+temp<=upper:
                temp+=temp
                n+=n
            upper-=temp
            res+=n 
        
        if (dividend<0 and divisor<0) or (dividend>0 and divisor>0):
            return res if res<2**31 else 2**31-1
        else:
            return -res if res>-2**31 else -2**31+1

"""
the following approach TLEd
"""

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor==0: 
            return MAX-INT
        elif dividend==0:
            return 0
        elif abs(divisor)==1:
            return dividend if divisor>0 else -dividend 
        upper, lower=abs(dividend), abs(divisor)
        n=0 
        while upper-lower >=lower:
            upper-=lower
            n+=1
        
        if (dividend<0 and divisor<0) or (dividend>0 and divisor>0):
            return n
        else:
            return -n