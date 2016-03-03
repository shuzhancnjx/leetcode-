# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 09:15:26 2015

@author: ZSHU
"""

"""
recursive algorithm/DFS
trimming conditions: s[0]!='0' and smaller than 256
"""


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        def ip(s, length, temp, res):
            if length==4 and s=='':
                res.append('.'.join(temp))
                return
            elif s=='' or length==4:
                return 
            else:
                if len(s)>0:
                    ip(s[1:], length+1, temp+[s[0]], res)
                if len(s)>=2 and s[0]!='0':
                    ip(s[2:],length+1, temp+[s[0:2]],res)
                if len(s)>=3 and s[0]!='0' and int(s[0:3])<256:
                    ip(s[3:], length+1, temp+[s[0:3]], res)
        
        res=[]
        ip(s, 0, [],res)
        return res 