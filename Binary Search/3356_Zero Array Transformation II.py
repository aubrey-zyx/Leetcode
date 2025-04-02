class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        def can_form_zero_array(k):
            difference = [0] * (n + 1)
            total = 0

            for i in range(k):
                start, end, val = queries[i]
                difference[start] += val
                difference[end + 1] -= val

            for i in range(n):
                total += difference[i]
                if total < nums[i]:
                    return False
            return True

        l, r = 0, len(queries)

        if not can_form_zero_array(r):
            return -1

        while l < r:
            m = l + (r - l) // 2
            if can_form_zero_array(m):
                r = m
            else:
                l = m + 1
        return l