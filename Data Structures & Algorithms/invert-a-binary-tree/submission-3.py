# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = []
        q.append(root)

        while q:
            node = q.pop(0)
            if node:
                if not node.left:
                    left=None
                else:
                    left = node.left
                if not node.right:
                    right=None
                else:
                    right = node.right
                node.right = left
                node.left = right
                q.append(node.right)
                q.append(node.left)
        return root

                
        