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