class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(left, right):
            i, j = left, right
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return checkPalindrome(left + 1, right) or checkPalindrome(left, right - 1)
        return True