# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        mp = {}
        child = set()

        for p, c, l in descriptions:
            if p not in mp:
                mp[p] = TreeNode(p)
            if c not in mp:
                mp[c] = TreeNode(c)

            if l:
                mp[p].left = mp[c]
            else:
                mp[p].right = mp[c]

            child.add(c)

        for p, _, _ in descriptions:
            if p not in child:
                return mp[p]