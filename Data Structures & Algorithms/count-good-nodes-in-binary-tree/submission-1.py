# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def isGood(node):
            path = []

            def dfs(node, target, path):
                if not node:
                    return False
                path.append(node.val)
                if node is target or dfs(node.left, target, path) or dfs(node.right, target, path):
                    return True
                path.pop()
                return False
            
            dfs(root, node, path)

            return all(n <= node.val for n in path)
        
        self.count = 0

        def dfs(node):
            if node:            
                if isGood(node):
                    self.count += 1
                
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        return self.count
                







