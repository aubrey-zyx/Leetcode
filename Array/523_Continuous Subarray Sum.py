class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pref_mod = 0
        mod_seen = {0: -1}
        for i, num in enumerate(nums):
            pref_mod = (pref_mod + num) % k
            if pref_mod in mod_seen:
                if mod_seen[pref_mod] <= i - 2:
                    return True
            else:
                mod_seen[pref_mod] = i
        return False