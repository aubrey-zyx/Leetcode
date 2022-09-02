class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(ch in set(jewels) for ch in stones)