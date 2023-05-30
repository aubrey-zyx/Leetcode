class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count_odd = self.expandFromCenter(s, i, i)
            count_even = self.expandFromCenter(s, i, i+1)
            count += count_odd + count_even
        return count

    def expandFromCenter(self, s, left, right):
        curr_count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            curr_count += 1
        return curr_count