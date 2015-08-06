# -*- coding: utf-8 -*-
"""
Created on Thu Aug 06 11:22:08 2015

@author: ZSHU
"""

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        pos, label, dic=[],{},{}
       
        for letter in t:
            label[letter]=label.get(letter, False)
            if dic.get(letter, 0)!=0:
                dic[letter][0]+=1
            else:
                dic[letter]=[1,0]
        
        window,p='',0
        while p<len(s):
            if dic.get(s[p],0)!=0:
                pos.append(p)
                dic[s[p]][1]+=1
                if dic[s[p]][0]<=dic[s[p]][1]:
                    label[s[p]]=True 
            while all(label.values())==True:
                temp=pos.pop(0)
                if window=='' or len(s[temp:p+1])<len(window):
                    window=s[temp:p+1]
                dic[s[temp]][1]-=1
                if dic[s[temp]][0]>dic[s[temp]][1]:
                    label[s[temp]]=False 
            p+=1
        return window
                    