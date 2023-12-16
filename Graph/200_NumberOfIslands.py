class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            visited.add((r, c))
            q = collections.deque()
            q.append((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            while q:
                row, col = q.popleft()
                for d in directions:
                    r, c = row + d[0], col + d[1]
                    if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visited:
                        visited.add((r, c))
                        q.append((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands