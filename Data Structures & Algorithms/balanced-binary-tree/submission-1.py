# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if node.val == 3:
                print(left, right)
            if abs(left - right) > 1:
                self.balanced += 1
            return 1 + max(left, right)
        dfs(root)
        return self.balanced < 1