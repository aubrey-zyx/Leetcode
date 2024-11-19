class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        path = 1
        queue = deque([(0, 0)])
        grid[0][0] = 1
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if (r, c) == (n - 1, n - 1):
                    return path
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(n) and nc in range(n) and grid[nr][nc] == 0:
                        queue.append((nr, nc))
                        grid[nr][nc] = 1
            path += 1

        return -1