# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node):
        if not node:
            return 0
        return 1 + max(self.dfs(node.left), self.dfs(node.right))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if abs(right - left) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False
        
        
