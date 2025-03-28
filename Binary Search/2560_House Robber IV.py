class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        low, high = min(nums), max(nums)
        n = len(nums)

        def is_achievable(cap):
            houses = 0
            i = 0
            while i < n:
                if nums[i] <= cap:
                    houses += 1
                    i += 2
                else:
                    i += 1
            return houses >= k

        while low < high:
            mid = low + (high - low) // 2
            if is_achievable(mid):
                high = mid
            else:
                low = mid + 1
        return low