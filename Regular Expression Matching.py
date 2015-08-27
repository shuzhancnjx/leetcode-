# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 14:56:07 2015

@author: ZSHU
"""



def match(s,p):
    i,j=0,0
    while j<len(s):
        if i<len(p) and p[i]!="*":
            if p[i]=="." or p[i]==s[j]:
                i+=1; j+=1 
            elif p[i]!=s[j]:
                if i+1<len(p) and p[i+1]=='*':
                    i+=1
                else:
                    return False 
        elif i<len(p) and p[i]=="*":
            k=j
            while k<len(s)-1 and s[k+1]==s[k]:
                k+=1
            for temp in range(k-j+2):
                if match(s[j:],temp*('' if i-1<0 else p[i-1])+p[i+1:]):
                    return True 
            return False 
        else:
            return False
        
    while i<len(p) and p[i]=="*":
        i+=1
    return i==len(p)

s='aa'
p='*a'

match(s,p)