# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.B = True
        self.lock = False
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if not self.lock: self.B = False if abs(left - right) > 1 else True
            if not self.B: self.lock = True
            return 1 + max(left, right)
        dfs(root)
    
        return self.B
