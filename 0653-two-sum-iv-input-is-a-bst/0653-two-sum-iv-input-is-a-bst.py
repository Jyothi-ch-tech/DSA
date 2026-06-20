# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        temp = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            temp.append(root.val)
            inorder(root.right)
        inorder(root)   # Missing call
        p1 = 0
        p2 = len(temp) - 1
        while p1 < p2:
            s = temp[p1] + temp[p2]
            if s == k:
                return True
            elif s < k:
                p1 += 1
            else:
                p2 -= 1
        return False