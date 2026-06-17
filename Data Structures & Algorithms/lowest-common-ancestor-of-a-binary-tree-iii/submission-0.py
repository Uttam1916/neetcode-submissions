"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def h(node):
            h=0 
            while node:
                h+=1
                node=node.parent
            return h
        h1,h2= h(p), h(q)
        if h1>h2:
            p,q=q,p
        dif= abs(h1-h2)
        while dif:
            q= q.parent
            dif-=1
        while p != q:
            p = p.parent
            q = q.parent

        return p