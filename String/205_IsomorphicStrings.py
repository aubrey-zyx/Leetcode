from collections import defaultdict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ht = defaultdict(str)
        for i in range(len(s)):
            if s[i] not in ht:
                if t[i] in ht.values():
                    return False
                else:
                    ht[s[i]] = t[i]
            else:
                if t[i] != ht[s[i]]:
                    return False
        return True