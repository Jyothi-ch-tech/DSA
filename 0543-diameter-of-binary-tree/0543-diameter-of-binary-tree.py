# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia=0
        def height(node):
            nonlocal dia
            if not node:
                return 0 
            l=height(node.left)
            r=height(node.right)
            ans=l+r
            dia=max(dia,ans)
            return max(l,r)+1
        height(root)
        return dia
        