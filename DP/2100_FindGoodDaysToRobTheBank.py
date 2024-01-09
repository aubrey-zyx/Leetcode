class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        non_decreasing = [1] * n
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                non_decreasing[i] = non_decreasing[i + 1] + 1
        non_increasing = 0
        res = []
        for i in range(n):
            if security[i] <= security[i - 1]:
                non_increasing += 1
            else:
                non_increasing = 1
            if non_increasing >= time + 1 and non_decreasing[i] >= time + 1:
                res.append(i)
        return res


class Solution2:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        left, right = [0] * n, [0] * n
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                left[i] = left[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                right[i] = right[i + 1] + 1
        return [i for i in range(time, n - time) if left[i] >= time and right[i] >= time]