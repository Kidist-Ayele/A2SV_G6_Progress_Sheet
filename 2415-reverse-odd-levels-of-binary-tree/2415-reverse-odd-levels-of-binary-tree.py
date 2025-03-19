# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node_left, node_right, level):
            if not (node_left and node_right):
                return 

            if level % 2:
                node_left.val, node_right.val = node_right.val, node_left.val

            dfs(node_left.left, node_right.right, level + 1)
            dfs(node_left.right, node_right.left, level + 1)


        dfs(root.left, root.right, 1)
        return root