# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(node, level, res):
            if not node:
                return
            if len(res) <= level:
                res.append([])
            res[level].append(node.val)
            bfs(node.left, level + 1, res)
            bfs(node.right, level + 1, res)
            return res

        l = bfs(root, 0, [])
        if not l: return []
        return [lst[-1] for lst in l]
