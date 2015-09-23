# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:02:43 2015

@author: ZSHU
"""
"""
recursive
"""

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def value(num, res): # this function is designed for properly evaluating the result for the "*" part
            if len(num)==0:
                return [0, res]
            p=len(num)-1; num1=int(num[p])
     
            while p-1>=0 and num[p-1]=="*":
                num2=int(num[p-2]); num1*=num2;p-=2
         
            if p==0: return [res-num1, num1]
            if num[p-1]=="+": return [res-num1,num1]
            if num[p-1]=="-": return [res+num1,-num1] # negative sign
            
        def add(temp, result, res, num):
            if result==target and len(num)==0:
                res.append(''.join(temp))
                return 
            elif len(num)==0: return 
            else:
                for i in range(len(num)):   
                    add(temp+['*']+[num[:i+1]], value(temp, result)[0]+ value(temp, result)[1]*int(num[:i+1]), res, num[i+1:])
                    add(temp+['+']+[num[:i+1]], result+int(num[:i+1]), res, num[i+1:])
                    add(temp+['-']+[num[:i+1]], result-int(num[:i+1]), res, num[i+1:])
                    if num[0]=='0': break # if zero, it can form a proper digit with the number(s) after it
             
        res=[]
        for i in range(len(num)):
            add([num[:i+1]], int(num[:i+1]), res, num[i+1:])
            if num[0]=='0': break 
        return res