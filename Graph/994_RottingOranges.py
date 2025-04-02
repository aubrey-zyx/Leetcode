class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rows, cols = len(grid), len(grid[0])
        minute = 0
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
            minute += 1

        return minute if fresh == 0 else -1