# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count=[]
        if not root:
            return 0
        q=deque([root])
        while q:
            node=q.popleft()
            count.append(node.val) 
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return len(count)       