from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        nei = defaultdict(list)
        for u, v in edges:
            nei[u].append(v)
            nei[v].append(u)

        vis = set()

        def dfs(node, parent):
            if node in vis:
                return False

            vis.add(node)
            for nxt in nei[node]:
                if nxt == parent:
                    continue
                if not dfs(nxt, node):
                    return False
            return True

        return dfs(0, -1) and len(vis) == n