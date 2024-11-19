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