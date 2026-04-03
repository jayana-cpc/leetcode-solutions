# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        
        if self.sameTree(root, subRoot):
            return True
        else:
            return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
    
    def sameTree(self, tree1, tree2):
        self.pL = []
        self.qL = []

        def dfs(node, l):
            if not node:
                l.append(None)
                return
            dfs(node.left, l)
            dfs(node.right, l)
            l.append(node.val)
            
        dfs(tree1, self.pL)
        dfs(tree2, self.qL)
        print(self.pL, self.qL)
        return self.pL == self.qL

        
                
