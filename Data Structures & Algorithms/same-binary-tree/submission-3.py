# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.pL = []
        self.qL = []

        def dfsP(node):
            if not node:
                self.pL.append(None)
                return
            dfsP(node.left)
            dfsP(node.right)
            self.pL.append(node.val)
            
        
        def dfsQ(node):
            if not node:
                self.qL.append(None)
                return
            dfsQ(node.left)
            dfsQ(node.right)
            self.qL.append(node.val)
            
        dfsP(p)
        dfsQ(q)
        print(self.pL, self.qL)
        return self.pL == self.qL

