# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def hei(root,h):
            if not root:
                return 0

            if root.right and root.left:
                return 1+max(hei(root.right,h+1),hei(root.left,h+1))
            elif root.right:
                return 1+ hei(root.right,h+1)
            else:
                return 1+ hei(root.left,h+1)
        return hei(root,0)