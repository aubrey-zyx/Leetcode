class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        board_copy = [row[:] for row in board]
        neighbors = [(-1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]

        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                for neighbor in neighbors:
                    r = row + neighbor[0]
                    c = col + neighbor[1]
                    if (r >= 0 and r < rows) and (c >= 0 and c < cols) and board_copy[r][c] == 1:
                        live_neighbors += 1
                if board_copy[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
                if board_copy[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1