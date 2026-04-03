# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # path
        ppath = []
        qpath = []

        def dfs(node, target, path):
            if not node:
                return False
            
            path.append(node)
            if node.val == target.val or dfs(node.left, target, path) or dfs(node.right, target, path):
                return True
            path.pop()
            return False
        
        dfs(root, p, ppath)
        dfs(root, q, qpath)
        print(ppath, qpath)
        i = 0
        minLen = min(len(ppath), len(qpath))
        while i < minLen and ppath[i] is qpath[i]:
            i += 1
        
        return ppath[i-1]