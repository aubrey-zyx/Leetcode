class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ht = collections.Counter(nums)
        ans = 0
        for num, cnt in ht.items():
            if k == 0:
                ans += (cnt >= 2)
            else:
                ans += (num + k in ht)
        return ans