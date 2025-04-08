# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        inorder(root)
        
        def findMid(left, right):
            if left > right:
                return 

            mid = left + (right - left) // 2
        
            new_tree = TreeNode(arr[mid])

            new_tree.left = findMid(left, mid - 1)
            new_tree.right = findMid(mid + 1, right)

            return new_tree
        
        ans = findMid(0, len(arr) - 1)
        return ans



        