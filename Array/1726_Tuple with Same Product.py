class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prod_freq = defaultdict(int)
        res = 0

        for i in range(n):
            for j in range(i + 1, n):
                prod = nums[i] * nums[j]
                prod_freq[prod] += 1

        for freq in prod_freq.values():
            pairs = freq * (freq - 1) // 2
            res += 8 * pairs

        return res