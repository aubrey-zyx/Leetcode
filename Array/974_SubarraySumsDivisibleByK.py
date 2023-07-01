class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        pref_mod = 0
        ht = collections.defaultdict(int)
        ht[0] = 1
        for num in nums:
            pref_mod = (pref_mod + num) % k
            ans += ht[pref_mod]
            ht[pref_mod] += 1
        return ans