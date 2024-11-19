class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        num = 1
        for layer in range((n + 1) // 2):
            for ptr in range(layer, n - layer):
                res[layer][ptr] = num
                num += 1
            for ptr in range(layer + 1, n - layer):
                res[ptr][n - layer - 1] = num
                num += 1
            for ptr in range(n - layer - 2, layer - 1, -1):
                res[n - layer - 1][ptr] = num
                num += 1
            for ptr in range(n - layer - 2, layer, -1):
                res[ptr][layer] = num
                num += 1
        return res