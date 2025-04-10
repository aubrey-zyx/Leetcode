class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                length += 1
            else:
                if length:
                    return length
        return length


class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()
        return len(arr[-1])