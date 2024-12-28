# Prefix Sum
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0
        ht = defaultdict(int)
        ht[0] = 1
        cur_sum = 0
        for num in nums:
            cur_sum += num
            res += ht[cur_sum - goal]
            ht[cur_sum] += 1
        return res


# Two-pass sliding window
class Solution2:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.sliding_win_at_most(nums, goal) - self.sliding_win_at_most(nums, goal - 1)
    
    def sliding_win_at_most(self, nums, goal):
        l, cur_sum, res = 0, 0, 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            while l <= r and cur_sum > goal:
                cur_sum -= nums[l]
                l += 1     
            res += r - l + 1
        return res

    

# One-pass sliding window
class Solution3:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        l = res = cur_sum = pref_zeroes = 0
        for r, num in enumerate(nums):
            cur_sum += num
            while l < r and (nums[l] == 0 or cur_sum > goal):
                if nums[l] == 1:
                    pref_zeroes = 0
                else:
                    pref_zeroes += 1
                cur_sum -= nums[l]
                l += 1
            if cur_sum == goal:
                res += 1 + pref_zeroes
        return res