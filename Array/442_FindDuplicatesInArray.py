class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                ans.append(abs(num))
            nums[abs(num) - 1] *= -1
        return ans


class Solution2:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                '''
                "nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]" does not work
                
                better:
                p=nums[i]
                nums[i], nums[p - 1] = nums[p - 1], nums[i]
                
                https://stackoverflow.com/questions/68152730/understand-python-swapping-why-is-a-b-b-a-not-always-equivalent-to-b-a-a
                '''
        return [num for i, num in enumerate(nums) if num - 1 != i]