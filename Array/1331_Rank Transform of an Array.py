class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = {}
        rank = 0
        for i, num in enumerate(sorted(arr)):
            if num not in d:
                rank += 1
            d[num] = rank
        return [d[num] for num in arr]