# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = [] # [1]
        q.append(root)
        ans = [] # [[1], ]
       
        while q:
            sub = [] # [2]
            for i in range(len(q)):
                node = q.pop(0) # 4
                if node:
                    sub.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if sub:
                ans.append(sub)

        return ans