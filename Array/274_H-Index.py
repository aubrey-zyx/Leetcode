class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        i = 0
        while i < len(citations) and citations[i] >= i + 1:
            i += 1
        return i


class Solution2:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        counter = [0] * (n + 1)
        for c in citations:
            if c >= n:
                counter[n] += 1
            else:
                counter[c] += 1
        total = 0
        for i in range(n, -1, -1):
            total += counter[i]
            if total >= i:
                return i
        return 0