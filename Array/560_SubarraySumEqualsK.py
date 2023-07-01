class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        prefsum = 0
        ht = collections.defaultdict(int)
        ht[0] = 1
        for num in nums:
            prefsum += num
            ans += ht[prefsum - k]
            ht[prefsum] += 1
        return ans