class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        i, j = 0, 1
        hashmap = {s[0]: 0}
        maxlen = 1
        while i < j and j < n:
            if s[j] in hashmap and hashmap[s[j]] >= i:
                i = hashmap[s[j]] + 1
            hashmap[s[j]] = j
            j += 1
            maxlen = max(maxlen, j - i)
        return maxlen


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        pos = {}
        for r in range(len(s)):
            if s[r] in pos and pos[s[r]] >= l:
                l = pos[s[r]] + 1
            pos[s[r]] = r
            res = max(res, r - l + 1)
        return res