class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        res = 0
        cur_end = float("-inf")
        for start, end in intervals:
            if start >= cur_end:
                cur_end = end
            else:
                res += 1
        return res