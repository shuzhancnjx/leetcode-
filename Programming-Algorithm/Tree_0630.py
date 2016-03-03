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
        
 

       
class Solution: 
    """ 
       purpose: these functions are devloped to address all the binary tree relataed 
       issues from Leetcode 
       thanks for the useful comments from internet 
    """
    
    def numTrees(self, n):
        """
        purpose: this function is to compute the number of all possible trees based on the catalan number
        n: the input, the number of nodes in the binary tree 
        by: zhan shu, shuzhancnjx@gmail.com         
        """
        dp=[1,1,2]
        if n<=2: return dp[n]
        else:
            dp +=[0 for i in range(n-2)]
            for i in range(3, n+1):
                for j in range(i):
                    dp[i] +=dp[j]*dp[i-j-1]
            return dp[n]

    def generateTrees(self, n):
        """
        purpose: this is a function to generate all possible binary trees based on n nodes
        n: the number of nodes 
        by: zhan shu, shuzhancnjx@gmail.com
        """
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
           purpose: this function is to perform inorder tranversial 
           root: the binary tree 
           res: the final result, start with []
           by: zhan shu, shuzhancnjx@gmail.com
        """
        if root==None:
            return 
        else:
            self.inorder_recursive(root.left, res)
            res+=[root.val] 
            self.inorder_recursive(root.right, res)
            return res
            
    def preorder_recursive(self, root, res):
        """
           purpose: this function is to perform perorder tranversial 
           root: the binary tree 
           res: the final result, start with []
           by: zhan shu, shuzhancnjx@gmail.com
        """
        if root==None:
            return 
        else:
            res+=[root.val]
            self.preorder_recursive(root.left, res)
            self.preorder_recursive(root.right, res)
            return res
            
    def postorder_recursive(self, root, res):
        """
           purpose: this function is to perform postorder tranversial 
           root: the binary tree 
           res: the final result, start with []
           by: zhan shu, shuzhancnjx@gmail.com
         """
        if root==None: return 
        else:
            self.postorder_recursive(root.left,res)
            self.postorder_recursive(root.right,res)
            res+=[root.val]
            return res
            
    def validTree(self, root):
        """
           purpose: this function is to verify a binary 
           root: the binary tree 
           by: zhan shu, shuzhancnjx@gmail.com
        """
        res=self.inorder_recursive(root,[])
        return res==sorted(res)
        
    def invert(self, root):
        """
           purpose: this function is to invert a binary tree 
           root: the binary tree 
           by: zhan shu, shuzhancnjx@gmail.com
         """
        if root.left==None and root.right==None:
            return root
        else: 
            left=self.invert(root.left)
            root.left=self.invert(root.right)
            root.right=left 
            return root    

    def pathTree(self, root):
        """
           purpose: this function is to return all possible pathes from the top to the deaf 
           root: the binary tree 
           by: zhan shu, shuzhancnjx@gmail.com
         """
        def path(root,pa):
            if root.left==None and root.right==None:
                res.append(pa[:])
                return 
            else:
                if root.left!=None:
                    path(root.left,pa+[root.left.val])
                if root.right!=None:
                    path(root.right,pa+[root.right.val])
        res=[]
        path(root, [root.val])
        return res

    def buildInPost(self, inorder, postorder):
        """
           purpose: this function is to build a binary tree based its inorder and postorder tranversial
           inorder: the inorder transverial result, a list 
           postorder: the postorder transverial result, a list 
           by: zhan shu, shuzhancnjx@gmail.com
        """
        if len(inorder)==0:
            return None
        else:
            root=Treenode(postorder[-1])
        
            i=0
            while i<len(inorder):
                if inorder[i]!=postorder[-1]:
                    i+=1
                else:
                    break   
            root.left=self.buildInPost(inorder[:i], postorder[:i])
            root.right=self.buildInPost(inorder[i+1:], postorder[i:(len(postorder)-1)])
            return root

    def isSystematic(self, root):
        """
           purpose: this function is to verify if a binary tree is systematic 
           root: the binary tree 
           by: zhan shu, shuzhancnjx@gmail.com
        """
        def sys(left, right):
            if left==None and right==None: 
                return True
            elif left==None or right==None:
                return False
            elif left.val!=right.val:
                return False
            else:
                return  sys(left.left, right.left) and  sys(left.right, right.right)
    
        if root==None: 
            return True 
        else:
            return sys(root.left, root.right)
           

    def sameTree(self, p, q):
        """
           purpose: this function is to test if two binary trees equal to each other 
           p: a binary tree 
           q: the other binary tree 
           by: zhan shu, shuzhancnjx@gmail.com
        """
        if p==None and q==None: 
            return True 
        elif p==None or q==None:
            return False 
        elif p.val!=q.val:
            return False 
        else:
            return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)

    def upsideDown(self, root):
        """
           purpose: this function is to upside down a binary tree with the constrains posted by Leetcode 
           root: the binary tree 
           by: zhan shu, shuzhancnjx@gmail.com
        """
        stack=[]
        while root.left:
            stack.append(root)
            root=root.left
        p=root 
        while stack:
            parent=stack.pop()
            root.left=parent.right
            root.right=parent 
            root=root.right
        root.left, root.right=None, None 
        return p

    def zzLevel(self, root):
        """
           purpose: this function is to perform a level-tranversial with zigzag outputs  
           root: the binary tree 
           by: zhan shu, shuzhancnjx@gmail.com
        """
        def zigzag(root, level, res):
            if root:
                if level>len(res)-1:
                    res+= [[] for i in range( level-len(res)+1)]
                if level%2==0: 
                    res[level].append(root.val)
                if level%2==1:
                    res[level].insert(0, root.val)
                zigzag(root.left, level+1, res)
                zigzag(root.right, level+1, res)
    
        level=0
        res=[[]]
        zigzag(root, level, res)
        return res
    
    def maxPathSum(self, root):
        """
           purpose: this function is to find out the maximum sum of any subtree  
           root: the binary tree 
           by: zhan shu, shuzhancnjx@gmail.com
        """
        def maxSum(root, maxvalue):
            if root==None:
                return 0
            else:
                temp=root.val
                left=maxSum(root.left, maxvalue)
                if left>0:
                    temp+=left
                right=maxSum(root.right, maxvalue)
                if right>0:
                    temp+=right
                        
                maxvalue[0]=max(maxvalue[0],temp)
                return max(root.val, max(root.val+left, root.val+right) )
                
       
        maxvalue=[root.val]
        maxSum(root, maxvalue)
        return maxvalue[0]
             
class Solution:
            
    def Depth(self, root):
        """
        purpose: this function is to return maximum and minimum depths, recursive functions
        root: the binary tree 
        by: zhan shu, shuzhancnjx@gmail.com
        """
        def mmdepth(root, depth, res):
            if root==None: 
                if depth>res[0]: res[0]=depth
                if depth<res[1]: res[1]=depth
                return
            else:
                mmdepth(root.left, depth+1, res)
                mmdepth(root.right, depth+1, res) 
                
        res=[0,100000]
        mmdepth(root1, 0, res)
        return {'the maximum depth': res[0], 'the minimum depth': res[1]}
        
        
        

"""
simple test cases 
"""
root1=Treenode(3)
root2=Treenode(9)
root3=Treenode(20)
root4=Treenode(15)
root5=Treenode(7)
root1.left=root2
root1.right=root3
root3.left=root4
root3.right=root5


Solution().numTrees(3)
Solution().generateTrees(3)
Solution().inorder_recursive(root1,[])
Solution().preorder_recursive(root1,[])
Solution().postorder_recursive(root1,[])
Solution().Depth(root1)
Solution().maxSum(root1)
Solution().zzLevel(root1)
Solution().upsideDown(root1)
Solution().sameTree(root1,root1)
Solution().isSystematic(root1)

"""
 the next are interative-based inorder, preorder and postorder transveral 
"""
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

        
class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        if root==None:
            return []
            
        visited=set()
        stack=[]
        res=[]
        while stack or root:
            if root in visited:
                res+=[root.val]
                if len(stack)>0:
                    root=stack.pop()
                else:
                    break
            else:
                if root:
                    stack+=[root]
                    if root.left and root.left not in visited:
                        root=root.left
                    elif root.right and root.right not in visited:
                        root=root.right
                    else:
                        visited.add(root)
                        stack.pop()
        return res 

def upsideDownI(root):
    p, parent, parent_right=root, None, None 
    
    while p:
        left=p.left
        p.left=parent_right
        parent_right=p.right
        p.right=parent
        parent=p
        p=left
    
    return parent 

def upsideDownII(root):
    
    def upside(p, parent):
        if p==None:
            return parent 
            
        ro=upside(p.left, p)
        if parent:
            p.left=parent.right
        else:
            p.left=None 
        p.right=parent 
        return ro
        
    return upside(root1, None)

def invertBinaryTree(root):
    stack=[]
    p=root
    while root or stack:
        if root:
            stack.append(root)
            root=root.left 
        else:
            root=stack.pop()
            left=root.left 
            root.left=root.right
            root.right=left
            root=root.left
    return p

"""
leetcode problem 
Populating Next Right Pointers in Each Node I and II, three different ways
"""

 def connect(root): 
     """ 
     this one exceed the time limit
     """
     
     def subconnect(a, b):
         if a==None or b==None:
             return 
         else: 
            a.next=b
            subconnect(a.left, a.right)
            subconnect(b.left, b.right)
            subconnect(a.right, b.left)
            return 
            
     if root==None: 
         return 
     else:
         subconnect(root.left, root.right)
         return root
 
class Solution:
    # @param root, a tree link node
    # @return nothing
     """ 
     this was accetped by the system, next right pointer in each node I
     """
    def connect(self, root):
        if root==None or root.left==None:
            return 
        else:
            root.left.next=root.right
            if root.next!=None:
                root.right.next=root.next.left 
            self.connect(root.left)
            self.connect(root.right)
            return 
        

class Solution:
    # @param root, a tree link node
    # @return nothing
     """ 
     this was accetped by the system, next right pointer in each node II
     based on level tranversial
     """
    def connect(self, root):
        
        def level(root, depth, res):
            if root==None:
                return
            else:
                if depth>len(res)-1:
                    res+= [[] for i in range(depth-len(res)+1)]
                
                if len(res[depth])>0:
                    res[depth][-1].next=root
                res[depth]+=[root]
                level(root.left, depth+1, res)
                level(root.right, depth+1, res)

        level(root, 0, [[]])
        return   
 
"""
recover binary tree.
this one is based on the inorder tranversial
"""
 class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def recoverTree(self, root):
        def inorder(root, res, temp):
            if root:
                inorder(root.left,res, temp)
                if len(temp)==0:
                    temp.append(root)
                else:
                    if root.val<temp[0].val:
                        if len(res)==0:
                            res+=[temp[0],root]
                        else:
                            res[1]=root

                    temp[0]=root  
                inorder(root.right,res, temp)
                return res
        res=inorder(root, [], [])
        res[0].val, res[1].val=res[1].val, res[0].val     
      
"""
the number of nodes in a complete binary tree
Soultion I; exceeded time limit 
"""        
class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        
        def transversial(root, res):
            if root:
                res+=[root.val]
                transversial(root.left,res)
                transversial(root.right,res)
        
        res=[]
        transversial(root, res)
        return len(res)   

"""
count the number of nodes in a complete binary tree, leetcode 
"""

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        
        def llevel(root, level):
            if root==None:
                return level
            else:
                l=0
                llevel(root.left, level)
                return l 
        
        def rlevel(root, level):
            if root==None:
                return level
            else:
                r=0
                r=rlevel(root.right, level+1)
                return r 
        
        def count(root):
            if root==None:
                return 0 
            else:
                r=rlevel(root, 0)
                l=llevel(root,0)
                if r==l:
                    return 2**r-1
                else: 
                    return 1+count(root.left)+count(root.right)
                
        return count(root)
        
















