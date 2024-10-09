class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rols, cols = len(rooms), len(rooms[0])
        queue = deque()
        visited = set()
        for r in range(rols):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        step = 0
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while queue:
            step += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rols and 0 <= ny < cols and (nx, ny) not in visited and rooms[nx][ny] > 0:
                        rooms[nx][ny] = step
                        queue.append((nx, ny))
                        visited.add((nx, ny))