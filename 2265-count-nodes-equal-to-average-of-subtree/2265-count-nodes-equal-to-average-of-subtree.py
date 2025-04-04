# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0
            
        average_count = 0
        
        def dfs(node):
            nonlocal average_count

            if not node:
                return (0, 0)
            
            if not node.left and not node.right:
                average_count += 1
                return (node.val, 1)
            
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            average = (left_sum + right_sum + node.val) // (left_count + right_count + 1)

            if node.val == average:
                average_count += 1
            
            return (left_sum + right_sum + node.val, left_count + right_count + 1)
            

        dfs(root)

        return average_count
        

            
        