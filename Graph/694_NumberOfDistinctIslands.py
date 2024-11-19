class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c, start, shape):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == 0:
                return

            grid[r][c] = 0
            shape.append((r - start[0], c - start[1]))

            dfs(r + 1, c, start, shape)
            dfs(r - 1, c, start, shape)
            dfs(r, c + 1, start, shape)
            dfs(r, c - 1, start, shape)

            return shape

        unique_islands = set()
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    island = tuple(dfs(r, c, (r, c), []))
                    if island not in unique_islands:
                        unique_islands.add(island)
                        res += 1
        return res