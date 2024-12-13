class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ht = defaultdict(int)
        res = 0
        for num in nums:
            res += ht[num]
            ht[num] += 1
        return res