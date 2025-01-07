class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most_k_distinct(k):
            ht = defaultdict(int)
            l = 0
            cnt = 0
            for r in range(len(nums)):
                ht[nums[r]] += 1
                while len(ht) > k:
                    ht[nums[l]] -= 1
                    if ht[nums[l]] == 0:
                        del ht[nums[l]]
                    l += 1
                cnt += r - l + 1
            return cnt

        return at_most_k_distinct(k) - at_most_k_distinct(k - 1)