from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = defaultdict(list)
        for str in strs:
            key = "".join(sorted(str))
            ht[key].append(str)
        return list(ht.values())