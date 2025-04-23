class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        start_r, start_c = next((r, c) for r in range(n) for c in range(n) if grid[r][c])

        def dfs(r, c):
            if r not in range(n) or c not in range(n) or grid[r][c] != 1:
                return
            grid[r][c] = 2
            queue.append((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(start_r, start_c)

        distance = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if 0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] == 1:
                            return distance
                        elif grid[nr][nc] == 0:
                            queue.append((nr, nc))
                            grid[nr][nc] = -1
            distance += 1

        return distance