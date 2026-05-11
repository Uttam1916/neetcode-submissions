# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        li=[]
        def trav(root,li):
            if not root:
                return
            trav(root.left,li)
            li.append(root.val)
            trav(root.right,li)
            
        trav(root,li)
        print(li)
        return li[k-1]