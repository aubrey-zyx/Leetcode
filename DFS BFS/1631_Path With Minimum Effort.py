# Binary Search + BFS
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        def can_reach_destination(effort):
            queue = deque([(0, 0)])
            visited = [[False] * cols for _ in range(rows)]
            visited[0][0] = True
            while queue:
                r, c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return True
                for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                        diff = abs(heights[nr][nc] - heights[r][c])
                        if diff <= effort:
                            queue.append((nr, nc))
                            visited[nr][nc] = True
            return False

        l, r = 0, 1000000
        while l < r:
            mid = (l + r) // 2
            if can_reach_destination(mid):
                r = mid
            else:
                l = mid + 1
        return l


# Binary Search + DFS
class Solution2:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def can_reach_destination(r, c, effort):
            if r == rows - 1 and c == cols - 1:
                return True
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    nr not in range(rows)
                    or nc not in range(cols)
                    or (nr, nc) in visited
                    or abs(heights[nr][nc] - heights[r][c]) > effort
                ):
                    continue
                if can_reach_destination(nr, nc, effort):
                    return True
            return False

        l, r = 0, 1000000
        while l < r:
            mid = (l + r) // 2
            visited = set()
            if can_reach_destination(0, 0, mid):
                r = mid
            else:
                l = mid + 1
        return l