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


class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""       
        for tmp in zip(*strs):
            if len(set(tmp)) == 1:
                res += tmp[0]
            else:
                break
        return res


class Solution3:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][:i]
        return strs[0]
