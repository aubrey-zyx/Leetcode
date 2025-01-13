# Prefix Array + Bit Masking
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        prefix_xor = [0] * n
        prefix_xor[0] = nums[0]
        for i in range(1, n):
            prefix_xor[i] = prefix_xor[i - 1] ^ nums[i]
        res = [0] * n
        mask = (1 << maximumBit) - 1
        for i in range(n):
            cur_xor = prefix_xor[n - 1 - i]
            res[i] = cur_xor ^ mask
        return res


# Optimized. O(1) space
class Solution2:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        xor_product = 0
        for i in range(n):
            xor_product = xor_product ^ nums[i]
        res = [0] * n
        mask = (1 << maximumBit) - 1
        for i in range(n):
            res[i] = xor_product ^ mask
            xor_product = xor_product ^ nums[n - 1 - i]
        return res