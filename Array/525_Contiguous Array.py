class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        ht = {0: -1}
        res = 0
        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                count -= 1
            if count in ht:
                res = max(res, i - ht[count])
            else:
                ht[count] = i
        return res