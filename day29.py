# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    def __init__(self):
        self.nodeMax = -float('inf')
    
    def traverse(self, A):
        if not A:
            return -1
            
        l, r = self.traverse(A.left) if A.left else 0, self.traverse(A.right) if A.right else 0
        path = max(A.val, A.val+l, A.val+r)
        self.nodeMax = max(self.nodeMax, max(path, A.val+l+r))
        
        return path
    
    # @param A : root node of tree
    # @return an integer
    def maxPathSum(self, A):
        self.traverse(A)
        return self.nodeMax
        
        
