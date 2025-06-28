class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = [None] * (n ** 2 + 1)
        num = 1
        cols = list(range(0, n))
        for r in range(n - 1, -1, -1):
            for c in cols:
                cells[num] = (r, c)
                num += 1
            cols.reverse()

        queue = deque([1])
        visited = set([1])
        step = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == n ** 2:
                    return step
                for nxt in range(cur + 1, min(cur + 6, n ** 2) + 1):
                    nr, nc = cells[nxt]
                    destination = board[nr][nc] if board[nr][nc] != -1 else nxt
                    if destination not in visited:
                        queue.append(destination)
                        visited.add(destination)
            step += 1

        return -1