class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r,c= len(grid), len(grid[0])
        INF=2147483647
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q=deque()
        visited = set()
        for i in range(r):
            for j in range(c):
                if grid[i][j]==0:
                    q.append([i,j])
                    visited.add((i,j))

        def addcell(i,j):
            if (min(i,j) < 0 or i == r or j == c or
                (i,j) in visited or grid[i][j] == -1):
                return
            visited.add((i,j))
            q.append([i,j])


        dist=0
        while q:
            for _ in range(len(q)):
                node=q.popleft()
                i,j= node[0],node[1]
                grid[i][j]=dist
                for dx,dy in directions:
                    addcell(i+dx,j+dy)
            dist+=1


