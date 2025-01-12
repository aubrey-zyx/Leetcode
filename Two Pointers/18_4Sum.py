class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums, target, k):
            res = []
            if not nums:
                return res

            average = target // k
            if nums[0] > average or nums[-1] < average:
                return res

            if k == 2:
                return twoSum(nums, target)

            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i - 1]:
                    for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)
            return res

        # Solution 1: two pointers
        def twoSum(nums, target):
            res = []
            l, r = 0, len(nums) - 1
            while l < r:
                total = nums[l] + nums[r]
                if total < target or (l > 0 and nums[l] == nums[l - 1]):
                    l += 1
                elif total > target or (r < len(nums) - 1 and nums[r] == nums[r + 1]):
                    r -= 1
                else:
                    res.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
            return res

        # Solution 2: hashset
        def twoSum_2(nums, target):
            res = []
            seen = set()
            for i in range(len(nums)):
                if res and nums[i] == res[-1][1]:
                    continue
                if target - nums[i] in seen:
                    res.append([target - nums[i], nums[i]])
                seen.add(nums[i])
            return res

        nums.sort()
        return kSum(nums, target, 4)