import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(' ', '')
        for i in string.punctuation:
            s = s.replace(i, '')
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True


class Solution2:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True


class Solution3:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c.isalnum()).lower()
        return s == s[::-1]
