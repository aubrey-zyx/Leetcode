from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        ht = defaultdict(str)
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in ht:
                if words[i] in ht.values():
                    return False
                else:
                    ht[pattern[i]] = words[i]
            else:
                if words[i] != ht[pattern[i]]:
                    return False
        return True


'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        return len(set(pattern)) == len(set(s)) == len(set(zip_longest(pattern, s)))
'''