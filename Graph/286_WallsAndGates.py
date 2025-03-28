class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        queue = deque()
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        steps = 0
        while queue:
            steps += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and rooms[nr][nc] > 0:
                        rooms[nr][nc] = steps
                        queue.append((nr, nc))
                        visited.add((nr, nc))