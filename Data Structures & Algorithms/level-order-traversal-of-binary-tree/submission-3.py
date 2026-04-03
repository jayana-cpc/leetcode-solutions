# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def bfs(node):
            q = [node]
            
            while q:
                qLen = len(q)
                level = []
                for i in range(qLen):
                    x = q.pop(0)
                    if x:
                        level.append(x.val)
                        q.append(x.left)
                        q.append(x.right)
                if level:
                    res.append(level)
        
        bfs(root)
        return res


