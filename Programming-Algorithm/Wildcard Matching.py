# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 09:09:15 2015

@author: ZSHU
"""
 
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p=="*" or p==s:
            return True 
        elif len(s)==0 or len(p)==0:
            return False 
        else:
            i=0
            while i<len(p):
                if p[i]!='*':
                    if p[i]=="?" or p[i]==s[i]:
                        return self.isMatch(s[i+1:],p[i+1:])
                    else:
                        return False 
                else:
                    for j in range(i, len(s)):
                        if self.isMatch(s[j:],p[i+1:]):
                            return True 
                    return False 
            return True 
            
"""
this solution above did not pass the follow test                
s="babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb"
p="*b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***b"           
"""
"""
this is a popular one from internet
http://chaoren.is-programmer.com/posts/42771.html
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p=="*" or p==s:
            return True 
        elif len(s)==0 or len(p)==0:
            return False 
        else:
            i=0
            while i<len(p):
                if p[i]!='*':
                    if p[i]=="?" or p[i]==s[i]:
                        return self.isMatch(s[i+1:],p[i+1:])
                    else:
                        return False 
                else:
                    for j in range(i, len(s)):
                        if self.isMatch(s[j:],p[i+1:]):
                            return True 
                    return False 
            return True 
        