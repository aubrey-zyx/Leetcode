import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt1 = collections.Counter(ransomNote)
        cnt2 = collections.Counter(magazine)
        for ch in cnt1:
            if cnt2[ch] < cnt1[ch]:
                return False
        return True