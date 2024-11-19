class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        res = float("inf")
        l = r = 0
        bit_counts = [0] * 32

        def update_bit_counts(num, delta):
            nonlocal bit_counts
            for pos in range(32):
                if num & (1 << pos):
                    bit_counts[pos] += delta

        def convert_bits_to_num(bit_counts):
            num = 0
            for pos in range(32):
                if bit_counts[pos]:
                    num |= 1 << pos
            return num

        for r in range(len(nums)):
            update_bit_counts(nums[r], 1)
            while l <= r and convert_bits_to_num(bit_counts) >= k:
                res = min(res, r - l + 1)
                update_bit_counts(nums[l], -1)
                l += 1

        return -1 if res == float("inf") else res