class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        vis = set()

        def bfs(node):
            vis.add(node)
            q=deque([node])
            while q:
                cur=q.popleft()
                for nei in adj[cur]:
                    if nei not in vis:
                        vis.add(nei)
                        q.append(nei)

        count = 0
        for node in range(n):          
            if node not in vis:
                count += 1
                bfs(node)

        return count