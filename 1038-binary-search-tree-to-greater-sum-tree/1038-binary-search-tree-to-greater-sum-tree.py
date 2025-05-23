# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0

        def reverseinorder(node):
            nonlocal total
            
            if not node:
                return
            
            reverseinorder(node.right)
            total += node.val
            node.val = total 
            reverseinorder(node.left)

        reverseinorder(root) 
        return root


        