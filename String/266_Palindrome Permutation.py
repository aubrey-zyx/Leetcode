class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        cnt = Counter(s)
        odd = 0
        for freq in cnt.values():
            if freq % 2 == 1:
                odd += 1
                if odd > 1:
                    return False
        return True