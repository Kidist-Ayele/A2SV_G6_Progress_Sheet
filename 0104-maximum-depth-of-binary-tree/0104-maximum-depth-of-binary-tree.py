# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        res = []
        count = 0

        def depth(root,count):
            if not root:
                return
                
            count += 1
            depth(root.left,count)
            depth(root.right,count)
            res.append(count)

        depth(root,count)
        return max(res) if res else 0
        
        