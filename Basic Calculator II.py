# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 13:14:31 2015

@author: ZSHU
"""

"""
this is a tedious problem: 
1) i wrote a small function cal to process the expression without * and /
2) i wrote a small function to process the string for removing the white space and grabe the digit properly 
in case some numbers have more than one digit
3) using stack to record the temperatory result. 
"""


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def cal(nums):
            stack=[]; i=0
            while i<len(nums):
                if str(nums[i]) not in "+-":
                    stack.append(nums[i])
                elif nums[i]=="+":
                    i+=1; stack.append(int(stack.pop())+int(nums[i]))
                elif nums[i]=="-":
                    i+=1; stack.append(int(stack.pop())-int(nums[i]))
                i+=1
            return int(stack[0])
        
        i=0; stack=[]
        while i<len(s):
            if s[i] in "+-*/":
                stack.append(s[i])
            elif s[i].isdigit(): 
                j=i
                while j<len(s) and s[j].isdigit():
                    j+=1
                stack.append(s[i:j]); i=j-1
            i+=1
            
        i=0; stack1=[]
        while i<len(stack):
           if stack[i].isdigit():
               if stack1==[]:
                    stack1.append(stack[i])
               elif stack1[-1] in"+-" and (i+1<len(stack) and stack[i+1] not in "*/"):
                    if stack1[-1]=="+":
                        stack1.pop(); stack1.append(int(stack1.pop())+int(stack[i]))
                    else:
                        stack1.pop(); stack1.append(int(stack1.pop())-int(stack[i]))
               else:
                    stack1.append(stack[i])
               i+=1
           elif stack[i] in "+-":
               stack1.append(stack[i])
               i+=1
           elif stack[i] in "*/":
               temp=int(stack1.pop())
               while i<len(stack) and stack[i] in "*/":
                   i+=1
                   if stack[i-1]=="*": temp*=int(stack[i])
                   else: temp/=int(stack[i])
                   i+=1
               tem1=[temp]
               while stack1!=[] and stack1[-1] in "+-":
                   tem1.insert(0, stack1.pop())
                   tem1.insert(0, stack1.pop())
               stack1.append(cal(tem1))
        return int(cal(stack1))