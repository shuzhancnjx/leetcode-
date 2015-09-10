# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 12:25:33 2015

@author: ZSHU
"""

'''

'.' means stay the current level 

'..' means going to the upper level of directory 

'''

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path=path.split('/')
        
        stack=[]
        for letter in path:
            if letter=='' or letter=='.':
                continue 
            elif letter=='..':
                if stack!=[]:
                    stack.pop()
            else:
                stack.append('/'+letter)
        if stack==[]:
            return '/'
        return ''.join(stack)
         
     
             