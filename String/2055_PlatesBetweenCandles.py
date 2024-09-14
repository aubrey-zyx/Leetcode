class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        presum = [0] * (n + 1)
        left, right = [-1] * n, [-1] * n
        res = []

        l = -1
        for i, c in enumerate(s):
            if c == "*":
                presum[i + 1] = presum[i] + 1
            else:
                presum[i + 1] = presum[i]
                l = i
            left[i] = l

        r = -1
        for i, c in enumerate(s[::-1]):
            if c == "|":
                r = n - 1 - i
            right[n - 1 - i] = r

        for q in queries:
            l_candle, r_candle = right[q[0]], left[q[1]]
            if l_candle >= 0 and r_candle >= 0 and l_candle < r_candle:
                res.append(presum[r_candle] - presum[l_candle])
            else:
                res.append(0)

        return res