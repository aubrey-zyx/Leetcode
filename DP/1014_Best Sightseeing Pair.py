class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = 0
        max_left_score = values[0]
        for i in range(1, len(values)):
            right_score = values[i] - i
            left_score = values[i] + i
            res = max(res, max_left_score + right_score)
            max_left_score = max(max_left_score, left_score)
        return res