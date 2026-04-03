# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []

        def bfs(node):
            q = [node]

            while q:
                qLen = len(q)
                level = []

                for _ in range(qLen):
                    x = q.pop(0)
                    if x:
                        q.extend([x.left, x.right])
                        level.append(x.val)
                if level:
                    self.res.append(level)
        bfs(root)
        return self.res