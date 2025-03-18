# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
   
        cur_max = root.val
        cur_min = root.val

        def traverse(node, cur_min, cur_max, res):

            if not node:
                return res
        
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            
            res = max(res, abs(cur_max - cur_min))

            left = traverse(node.left, cur_min, cur_max, res)
            right = traverse(node.right, cur_min, cur_max, res)

            return max(left, right)
        
        return traverse(root, cur_min, cur_max, 0)

        