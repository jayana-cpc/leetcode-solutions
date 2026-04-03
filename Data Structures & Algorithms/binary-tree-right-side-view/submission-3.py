# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        def bfs(node):
            q = [node]

            while q:
                level = []
                qLen = len(q)

                for i in range(qLen):
                    x = q.pop(0)
                    if x:
                        q.append(x.left)
                        q.append(x.right)
                        level.append(x.val)
                if level:
                    self.res.append(level[-1])
        bfs(root)
        return self.res
