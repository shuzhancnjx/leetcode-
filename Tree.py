# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 16:04:03 2015

@author: ZSHU
"""

# this set code was devloped to address questions about Tree in leetcode. 

class Treenode:
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right=None 
        
 
root1=Treenode(3)
root2=Treenode(9)
root3=Treenode(20)
root4=Treenode(15)
root5=Treenode(7)
root1.left=root2
root1.right=root3
root3.left=root4
root3.right=root5
       
class Solution: 
    """ 
       purpose: these functions are devloped to address all the binary tree relataed 
       issues from Leetcode 
       thanks for the useful comments from internet 
    """
    
    def numTrees(self, n):
        dp=[1,1,2]
        if n<=2: return dp[n]
        else:
            dp +=[0 for i in range(n-2)]
            for i in range(3, n+1):
                for j in range(i):
                    dp[i] +=dp[j]*dp[i-j-1]
            return dp[n]

    def generateTrees(self, n):
        nums=range(1,n+1)
        def generate(nums):
            if len(nums)==0: return [None]
            else:
                res=[]
                for k in range(len(nums)):
                    treeleft=generate(nums[:k])
                    treeright=generate(nums[k+1:])
                    for i in treeleft:
                        for j in treeright:
                            root=Treenode(nums[k])
                            root.left=i
                            root.right=j
                            res.append(root)
                return res
        return generate(nums)
    
    def inorder_recursive(self, root, res):
        """
           this is a recursive solution        
        """
        if root==None:
            return 
        else:
            self.inorder_recursive(root.left, res)
            res+=[root.val] 
            self.inorder_recursive(root.right, res)
            return res
            
    def preorder_recursive(self, root, res):
        if root==None: return 
        else:
            res+=[root.val]
            self.preorder_recursive(root.left, res)
            self.preorder_recursive(root.right, res)
            return res
            
    def postorder_recursive(self, root, res):
        if root==None: return 
        else:
            self.postorder_recursive(root.left,res)
            self.postorder_recursive(root.right,res)
            res+=[root.val]
            return res 



Solution().numTrees(3)
Solution().generateTrees(3)
Solution().inorder_recursive(root1,[])
Solution().preorder_recursive(root1,[])
Solution().postorder_recursive(root1,[])


def inorderIter(root):
        inorder=[]
        stack=[]
        while root or stack:
            if root:
                stack+=[root]
                root=root.left
            else:
                root=stack.pop()
                inorder+=[root.val]
                root=root.right
        return inorder

def preorder(root):
    preorder=[]
    stack=[]
    while root or stack:
        if root:
            preorder+=[root.val]
            stack+=[root]
            root=root.left
        else:
            root=stack.pop()
            root=root.right
    return preorder
        
def postorder(root):
    postorder=[]
    stack=[]
    while root.left or root.right or stack:
        stack+=[root]
        if root.left:
            root=root.left     
        elif root.right:
            root=root.right   
        else:
            stack.pop()
            postorder+=[root.val]
            root=stack.pop()
    return postorder
        
            

































