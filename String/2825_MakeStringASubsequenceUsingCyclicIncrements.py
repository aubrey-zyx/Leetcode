class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = j = 0
        while i < len(str1) and j < len(str2):
            c1, c2 = str1[i], str2[j]
            if c1 == c2 or ord(c1) + 1 == ord(c2) or (c1 == "z" and c2 == "a"):
                j += 1
            i += 1
        return j == len(str2)