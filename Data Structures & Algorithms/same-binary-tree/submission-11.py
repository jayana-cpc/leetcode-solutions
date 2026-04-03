# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.same = 0
        def dfs(t1, t2):
            if (not t1 and t2) or (t1 and not t2):
                self.same += 1
                return 0
            if not t1 and not t2:
                return 0
            if t1.val != t2.val:
                self.same += 1
            return dfs(t1.left, t2.left) or dfs(t1.right, t2.right)
        dfs(p, q)
        return self.same < 1