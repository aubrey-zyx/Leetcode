class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k:
            return False
        if n == k:
            return True
        cnt = Counter(s)
        odd = 0
        for freq in cnt.values():
            if freq % 2 == 1:
                odd += 1
        return odd <= k