from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        str_min = min(strs)
        str_max = max(strs)
        for i, c in enumerate(str_min):
            if c != str_max[i]:
                return str_max[:i]
        return str_min

'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""       
        for tmp in zip(*strs):
            if len(set(tmp)) == 1:
                res += tmp[0]
            else:
                break
        return res
'''