class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = defaultdict(int)
        for c in text:
            if c in "balon":
                cnt[c] += 1
        if len(cnt) < 5:
            return 0
        cnt['l'] //= 2
        cnt['o'] //= 2
        return min(cnt.values())