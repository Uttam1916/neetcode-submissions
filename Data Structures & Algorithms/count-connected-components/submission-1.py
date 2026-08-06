class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        vis = set()

        def dfs(node):
            vis.add(node)
            for nei in adj[node]:
                if nei not in vis:
                    dfs(nei)

        count = 0
        for node in range(n):          
            if node not in vis:
                count += 1
                dfs(node)

        return count