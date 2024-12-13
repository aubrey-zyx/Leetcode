class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        rows, cols = len(board), len(board[0])
        queue = deque([click])
        visited = set(tuple(click))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                mine_cnt = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and board[nr][nc] == 'M':
                        mine_cnt += 1
                if mine_cnt > 0:
                    board[r][c] = str(mine_cnt)
                else:
                    board[r][c] = 'B'
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if nr in range(rows) and nc in range(cols) and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            queue.append([nr, nc])
        return board