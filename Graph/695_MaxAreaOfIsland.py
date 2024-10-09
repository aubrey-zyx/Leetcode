class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if (
                r < 0
                or r == rows
                or c < 0
                or c == cols
                or grid[r][c] == 0
                or (r, c) in visited
            ):
                return 0
            visited.add((r, c))
            return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)

        area = 0
        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r, c))
        return area


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            queue = [(r, c)]
            grid[r][c] = 0
            area = 1
            while queue:
                x, y = queue.pop(0)
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        area += 1
                        grid[nx][ny] = 0
                        queue.append((nx, ny))
            return area

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, bfs(r, c))
        return res