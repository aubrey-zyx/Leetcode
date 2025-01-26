class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        prefix_xor = 0
        vowel_mask = {"a": 1, "e": 2, "i": 4, "o": 8, "u": 16}
        xor_position = {0: -1}
        res = 0
        for i, c in enumerate(s):
            if c in "aeiou":
                prefix_xor ^= vowel_mask[c]
            if prefix_xor not in xor_position:
                xor_position[prefix_xor] = i
            res = max(res, i - xor_position[prefix_xor])
        return res