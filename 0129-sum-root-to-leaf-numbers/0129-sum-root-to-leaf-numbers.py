# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        arr = []
        ans = 0

        def dfs(node):
            nonlocal ans
            if not node:
                return

            if not node.left and not node.right:
                arr.append(str(node.val))
                ans += int(''.join(arr))
                arr.pop()
                return 
            
            arr.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            arr.pop()
            return 
        dfs(root)
        return ans
        