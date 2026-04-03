# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def largestNode(node):
            if not node:
                return float("-inf")
            return max(node.val, largestNode(node.left), largestNode(node.right))
        
        def smallestNode(node):
            if not node:
                return float("inf")
            return min(node.val, smallestNode(node.left), smallestNode(node.right))

        self.valid = True
        def dfs(node):
            if node:
                left = largestNode(node.left)
                right = smallestNode(node.right)
                
                if not (left < node.val < right):
                    self.valid = False
                    return
                
                dfs(node.left)
                dfs(node.right)
            return
        
        dfs(root)
        return self.valid
            
