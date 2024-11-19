class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        n = len(digits)
        if n < 2:
            return num

        right_max_val = digits[-1]
        right_max_idx = n - 1
        l = r = n
        for i in range(n - 2, -1, -1):
            if digits[i] < right_max_val:
                l = i
                r = right_max_idx
            elif digits[i] > right_max_val:
                right_max_val = digits[i]
                right_max_idx = i

        if l == n:
            return num

        digits[l], digits[r] = digits[r], digits[l]
        return int("".join(digits))