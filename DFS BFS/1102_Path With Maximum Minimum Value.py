# Binary Search + BFS
class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def path_exists(score):
            queue = deque([(0, 0)])
            visited = set([(0, 0)])
            while queue:
                r, c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and (nr, nc) not in visited
                            and grid[nr][nc] >= score
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return False

        l = 0
        r = min(grid[0][0], grid[-1][-1])
        res = 0
        while l <= r:
            m = (l + r) // 2
            if path_exists(m):
                res = m
                l = m + 1
            else:
                r = m - 1
        return res


# Binary Search + DFS
class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def path_exists(score):
            visited = set()

            def dfs(r, c):
                if (r, c) == (rows - 1, cols - 1):
                    return True
                visited.add((r, c))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and (nr, nc) not in visited
                            and grid[nr][nc] >= score
                            and dfs(nr, nc)
                    ):
                        return True
                return False

            return dfs(0, 0)

        l = 0
        r = min(grid[0][0], grid[-1][-1])
        res = 0
        while l <= r:
            m = (l + r) // 2
            if path_exists(m):
                res = m
                l = m + 1
            else:
                r = m - 1
        return res