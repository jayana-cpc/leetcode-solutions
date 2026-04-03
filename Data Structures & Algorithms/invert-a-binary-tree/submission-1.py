# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # purpose of the queue is to hold whats on a level
        q = []
        head = root
        q.append(root)
        # q = [1]
        while q:
            """
            1
           / \
          2  null
            """
            for _ in range(len(q)):
                node = q.pop(0)
                # if node and node.right is not None and node.left is not None:
                if node:
                    if node.right:
                        right = node.right
                    else:
                        right = None
                    if node.left:
                        left = node.left
                    else:
                        left = None                    
                    node.right = left
                    node.left = right
                    q.append(node.left)
                    q.append(node.right)
        return head


