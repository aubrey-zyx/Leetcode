class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        q = collections.deque()
        q.append((0, 0))
        visited = set()
        visited.add((0, 0))
        x, y = abs(x), abs(y)
        directions = [[2, 1], [2, -1], [1, 2], [1, -2], [-2, 1], [-2, -1], [-1, 2], [-1, -2]]
        step = 0

        while q:
            for _ in range(len(q)):
                old_x, old_y = q.popleft()
                if (old_x, old_y) == (x, y):
                    return step
                for dx, dy in directions:
                    new_x, new_y = old_x + dx, old_y + dy
                    if new_x >= -2 and new_y >= -2 and (new_x, new_y) not in visited:
                        visited.add((new_x, new_y))
                        q.append((new_x, new_y))
            step += 1

        return step


class Solution2:
    def minKnightMoves(self, x: int, y: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(x, y):
            if x + y == 0:
                return 0
            elif x + y == 2:
                return 2
            else:
                return min(dfs(abs(x - 1), abs(y - 2)), dfs(abs(x - 2), abs(y - 1))) + 1
        return dfs(abs(x), abs(y))