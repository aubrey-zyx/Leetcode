class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(r, c, i):
            if board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True

            path.add((r, c))
            res = False
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in path:
                    if dfs(nr, nc, i + 1):
                        res = True
                        break
            path.remove((r, c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False