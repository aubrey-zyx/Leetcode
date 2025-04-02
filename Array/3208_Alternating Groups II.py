class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        res = 0
        cnt = 1
        prev_color = colors[0]

        for i in range(1, n + k - 1):
            i %= n
            if colors[i] == prev_color:
                cnt = 1
                prev_color = colors[i]
                continue
            cnt += 1
            if cnt >= k:
                res += 1
            prev_color = colors[i]

        return res