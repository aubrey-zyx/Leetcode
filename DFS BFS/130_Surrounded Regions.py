class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        borders = []
        for r in range(rows):
            if r == 0 or r == rows - 1:
                for c in range(cols):
                    borders.append((r, c))
            else:
                borders.append((r, 0))
                borders.append((r, cols - 1))

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or board[r][c] != "O":
                return
            board[r][c] = "E"
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)

        for r, c in borders:
            dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "E":
                    board[r][c] = "O"


# BFS
class Solution2:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        borders = []
        for r in range(rows):
            if r == 0 or r == rows - 1:
                for c in range(cols):
                    borders.append((r, c))
            else:
                borders.append((r, 0))
                borders.append((r, cols - 1))

        def bfs(r, c):
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            queue = deque([(r, c)])
            while queue:
                row, col = queue.popleft()    # Change it to pop() then it will be DFS done in iteration
                if board[row][col] != "O":
                    continue
                board[row][col] = "E"
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                        queue.append((nr, nc))

        for r, c in borders:
            bfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "E":
                    board[r][c] = "O"