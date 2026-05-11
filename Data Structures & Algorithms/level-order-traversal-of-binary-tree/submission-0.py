from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            vals = []
            nodes = []

            # process only current level
            for _ in range(len(q)):
                new = q.popleft()
                nodes.append(new)
                vals.append(new.val)

            for node in nodes:
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            res.append(vals)

        return res