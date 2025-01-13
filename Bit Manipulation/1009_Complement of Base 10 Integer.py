class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        todo, bit = n, 1
        while todo:
            n = n ^ bit
            bit <<= 1
            todo >>= 1
        return n


class Solution2:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        length = floor(log2(n)) + 1
        bitmask = (1 << length) - 1
        return n ^ bitmask