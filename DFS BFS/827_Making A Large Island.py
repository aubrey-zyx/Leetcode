class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def dfs(r, c, id):
            area = 1
            grid[r][c] = id
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    area += dfs(nr, nc, id)
            return area

        id = 2
        areas = {}
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    areas[id] = dfs(r, c, id)
                    id += 1

        res = max(areas.values() or [0])
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    ids = set()
                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            ids.add(grid[nr][nc])
                        res = max(res, 1 + sum(areas[id] for id in ids))
        return res