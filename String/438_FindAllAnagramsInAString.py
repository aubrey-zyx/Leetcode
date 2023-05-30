from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        if s_len < p_len:
            return []
        ans = []
        s_count = [0] * 26
        p_count = [0] * 26
        for i in range(p_len):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1
        if s_count == p_count:
            ans.append(0)
        for i in range(s_len - p_len):
            s_count[ord(s[i]) - 97] -= 1
            s_count[ord(s[i + p_len]) - 97] += 1
            if s_count == p_count:
                ans.append(i + 1)
        return ans


class Solution2:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        chars = set(p)
        cnt_p = Counter(p)
        ans = []
        for i in range(len(s) - n + 1):
            if s[i] not in chars:
                continue
            if Counter(s[i:i+n]) == cnt_p:
                ans.append(i)
        return ans