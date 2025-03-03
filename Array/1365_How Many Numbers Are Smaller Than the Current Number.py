class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = {}
        for i, num in enumerate(sorted(nums)):
            if num not in d:
                d[num] = i
        res = [d[num] for num in nums]
        return res


# O(n)
class Solution2:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cnt = [0] * 101
        for num in nums:
            cnt[num] += 1
        for i in range(1, 101):
            cnt[i] += cnt[i - 1]
        res = []
        for num in nums:
            res.append(cnt[num - 1] if num > 0 else 0)
        return res