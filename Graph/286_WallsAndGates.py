class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        queue = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        INF = 2 ** 31 - 1

        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    queue.append((r, c))

        distance = 0
        while queue:
            distance += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and rooms[nr][nc] == INF:
                        rooms[nr][nc] = distance
                        queue.append((nr, nc))