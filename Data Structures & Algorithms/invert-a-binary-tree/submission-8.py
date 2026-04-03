# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs(node):
            q = [node]

            while q:
                thing = q.pop(0)
                if thing:
                    thing.left, thing.right = thing.right, thing.left
                    q.append(thing.left)
                    q.append(thing.right)
            
        bfs(root)
        return root