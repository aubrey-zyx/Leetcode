class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarray_sums = []
        n = len(nums)
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                subarray_sums.append(total)
        subarray_sums.sort()
        res = 0
        mod = 10 ** 9 + 7
        for i in range(left - 1, right):
            res = (res + subarray_sums[i]) % mod
        return res


class Solution2:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        heap = []
        for i in range(n):
            heapq.heappush(heap, (nums[i], i))
        res = 0
        mod = 10 ** 9 + 7
        for i in range(1, right + 1):
            total, end = heapq.heappop(heap)
            if i >= left:
                res = (res + total) % mod
            if end < n - 1:
                heapq.heappush(heap, (total + nums[end + 1], end + 1))
        return res