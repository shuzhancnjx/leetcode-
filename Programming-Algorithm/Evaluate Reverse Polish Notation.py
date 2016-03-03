# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 08:59:30 2015

@author: ZSHU
"""

"""
implementing Stack 
"""

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]; operator=["+","-","*","/"]
        for letter in tokens:
            if letter not in operator:
                stack.append(int(letter))
            else:
                num1=stack.pop(); num2=stack.pop()
                if letter=="*":
                    stack.append(num1*num2)
                elif letter=="+":
                    stack.append(num1+num2)
                elif letter=="-":
                    stack.append(num2-num1)
                elif letter=="/":
                    sign=1
                    if num2<0: sign*=-1; num2=-1*num2
                    if num1<0: sign*=-1; num1=-1*num1
                    stack.append(sign*(num2/num1))
        return stack[0]