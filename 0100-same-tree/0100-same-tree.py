# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree1 = []
        tree2 = []
      

        def traverse1(node):
            if not node:
                tree1.append(None)
                return 
            tree1.append(node.val)
            traverse1(node.left)
            traverse1(node.right)
        traverse1(p)

        def traverse2(node2):
            if not node2:
                tree2.append(None)
                return 

            tree2.append(node2.val)
            traverse2(node2.left)
            traverse2(node2.right)
        traverse2(q)
    
        return tree1 == tree2
