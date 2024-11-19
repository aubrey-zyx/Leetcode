class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if abs(target - total) < abs(diff):
                    diff = target - total
                if diff == 0:
                    return target
                if target > total:
                    l += 1
                else:
                    r -= 1
        return target - diff