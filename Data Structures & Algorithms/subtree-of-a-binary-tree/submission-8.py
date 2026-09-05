# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p, q):
            def dfs(p, q):
                if not p and not q:
                    return True
                elif p and q and p.val == q.val:
                    return dfs(p.left, q.left) and dfs(p.right, q.right)
                return False
            return dfs(p, q)
        
        def dfs(node):
            if not node:
                return False
            
            same = sameTree(node, subRoot)

            if same:
                return True
            return dfs(node.left) or dfs(node.right)
        return dfs(root)
        