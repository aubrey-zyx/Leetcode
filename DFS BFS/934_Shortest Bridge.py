class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        start_x, start_y = -1, -1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    start_x, start_y = i, j
                    break

        def dfs(x, y):
            if x not in range(n) or y not in range(n) or grid[x][y] != 1:
                return
            grid[x][y] = 2
            queue.append((x, y))
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        queue = deque()
        dfs(start_x, start_y)

        distance = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if nx in range(n) and ny in range(n):
                        if grid[nx][ny] == 1:
                            return distance
                        elif grid[nx][ny] == 0:
                            queue.append((nx, ny))
                            grid[nx][ny] = -1
            distance += 1
        return distance