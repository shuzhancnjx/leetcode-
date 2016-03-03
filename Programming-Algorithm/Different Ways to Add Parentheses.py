# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 13:03:36 2015

@author: ZSHU
"""

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        def add( res, pattern, visited):
            if len(pattern)==1 and pattern[0] not in visited :
                visited+=pattern
                res+=[eval(pattern[0])]
                return 
            else:
                for i in range(len(pattern)):
                    if pattern[i] in ["*","+","-"]: 
                        if pattern[i]=="*": 
                            add(res,pattern[:i-1]+['('+str(pattern[i-1])+str(pattern[i])+str(pattern[i+1])+')']+pattern[i+2:],visited)
                        elif pattern[i]=="+":  
                            add(res,pattern[:i-1]+['('+str(pattern[i-1])+str(pattern[i])+str(pattern[i+1])+')']+pattern[i+2:],visited)
                        elif pattern[i]=="-": 
                            add(res,pattern[:i-1]+['('+str(pattern[i-1])+str(pattern[i])+str(pattern[i+1])+')']+pattern[i+2:],visited)
        
        
        res=[]; numslist=[];visited=[]
        numslist=re.split('(\D)',input)
        add(res, numslist, visited)
        return res        
     