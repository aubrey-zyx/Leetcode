class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = []
        r, c = rStart, cStart
        step = 1
        d = 0
        while len(res) < rows * cols:
            for _ in range(2):
                for _ in range(step):
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])
                    r += directions[d][0]
                    c += directions[d][1]
                d = (d + 1) % 4
            step += 1
        return res