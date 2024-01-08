class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        row, col = len(grid), len(grid[0])
        q = collections.deque()
        minute = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while q and fresh > 0:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dr, dc in directions:
                    r, c = x + dr, y + dc
                    if r in range(row) and c in range(col) and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append((r, c))
                        fresh -= 1
            minute += 1

        return minute if fresh == 0 else -1