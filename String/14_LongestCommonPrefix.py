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


# Vertical Scanning
class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][:i]
        return strs[0]


# Horizontal Scanning
class Solution3:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix
