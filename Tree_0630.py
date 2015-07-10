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
            
    def validTree(self, root):
        res=self.inorder_recursive(root,[])
        return res==sorted(res)
        
        

Solution().numTrees(3)
Solution().generateTrees(3)
Solution().inorder_recursive(root1,[])
Solution().preorder_recursive(root1,[])
Solution().postorder_recursive(root1,[])

"""
 the next three are interative-based inorder, preorder and postorder transveral 
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

        
def postorder(root):
    postorder=[]
    visited=set()
    stack=[]
    
    while root or stack:
        if root and root not in visited:
            stack+=[root]
            if root.left!=None and root.left not in visited:
                root=root.left
            elif root.right!=None and root.right not in visited:
                root=root.right
            else:
                visited.add(root)
                stack.pop()
        else:
            postorder+=[root.val]
            if len(stack)>0:
                root=stack.pop()
            else:
                break
    return postorder

"""
 a sysmetic tree
"""

root1=Treenode(1)
root2=Treenode(2)
root3=Treenode(2)
root4=Treenode(3)
root5=Treenode(3)
root6=Treenode(4)
root7=Treenode(4)
root8=Treenode(5)
root1.left=root2
root1.right=root3
root2.left=root4
root2.right=root6
root3.left=root5
root3.right=root7


def isSystematic(root):
    
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
           

def sameTree(p, q):
    if p==None and q==None: 
        return True 
    elif p==None or q==None:
        return False 
    elif p.val!=q.val:
        return False 
    else:
        return sameTree(p.left, q.left) and sameTree(p.right, q.right)
               
"""
a sample tree for zigzag level ordering 
"""
root1=Treenode(1)
root2=Treenode(2)
root3=Treenode(3)
root4=Treenode(4)
root5=Treenode(5)
root6=Treenode(6)
root7=Treenode(7)
root8=Treenode(8)
root9=Treenode(9)
root1.left=root2
root1.right=root3
root2.left=root4
root2.right=root5
root3.left=root6
root3.right=root7
root6.left=root8
root6.right=root9
root4.left=Treenode(0)

def zzLevel(root):
    
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
"""
in the recursive functions, how to save the results at each step is really important, 
1) the data type in return, single number, list, or other 
2) using global variable or local variable to save the results of each step 

the zigzag and pathTree are two typical examples. 
"""         

def pathTree(root):
    
    def path(root,pa):
        if root.left==None and root.right==None:
            res.append(pa[:])
            return 
        else:
            if root.left!=None:
"""
note: the variable pa only exists in the path function, not accumulated across left and right tree
"""
                path(root.left,pa+[root.left.val])
            if root.right!=None:
                path(root.right,pa+[root.right.val])
    res=[]
    path(root, [root.val])
    return res 

root1=Treenode(1)
root2=Treenode(2)
root3=Treenode(3)
root1.left=root2
root1.right=root3

"""
maximum path, thanks the post from internet. 
"""

def maxSum(root):
    def maxPath(root,ma):
        if root.left==None and root.right==None:
            return root.val
        else:
            temp=root.val; lmax=0;rmax=0
            if root.left!=None:
                lmax=maxPath(root.left,ma)
                if lmax>0:
                    temp+=lmax
            if root.right!=None:
                rmax=maxPath(root.right,ma)
                if rmax>0:
                    temp+=rmax
            if temp>ma: ma=temp
            return max(max(root.val+lmax, root.val+rmax), root.val)
        
    if root==None: 
        return 0
    else:
        maxPath(root,-1000000)
    return ma
 
"""
maximum and minimum depths, recursive functions
"""   
def Depth(root):
    def mmdepth(root, depth):
        global maxdepth, mindepthdf
        if root==None: 
            if depth>maxdepth: maxdepth=depth
            if depth<mindepth: mindepth=depth
            return
        else: 
            mmdepth(root.left, depth+1)
            mmdepth(root.right, depth+1)
            return [maxdepth,mindepth]
    maxdepth=-1
    mindepth=100**100  
    return mmdepth(root, 0)

"""
upside down, three methods, iteration, recursive, and traversial 
"""
root1=Treenode(1)
root2=Treenode(2)
root3=Treenode(3)
root4=Treenode(4)
root5=Treenode(5)
root1.left=root2
root1.right=root3
root2.left=root4
root2.right=root5


root=root1

def upDownIII(root):
    
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


def buildInPost(inorder, postorder):
    
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
            
        root.left=buildInPost(inorder[:i], postorder[:i])
        root.right=buildInPost(inorder[i+1:], postorder[i:(len(postorder)-1)])
        
        return root
    
"""
invert binary tree by iteration and recursive functions 
by zhan shu, shuzhancnjx@gmail.com

"""

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



           
root1=Treenode(1)
root2=Treenode(2)
root3=Treenode(3)
root4=Treenode(4)
root5=Treenode(5)
root1.left=root2
root1.right=root3
root2.left=root4
root2.right=root5            
         
def invert(root):
    if root.left==None and root.right==None:
        return root
    else: 
        left=invert(root.left)
        root.left=invert(root.right)
        root.right=left 
        return root
        
        
          
            
            
        
 
        

        
    
    
  

      
        
        

























