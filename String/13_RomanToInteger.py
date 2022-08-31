class Solution:
    def romanToInt(self, s: str) -> int:
        ht = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        for i in range(len(s) - 1):
            if ht[s[i]] >= ht[s[i+1]]:
                num += ht[s[i]]
            else:
                num -= ht[s[i]]
        num += ht[s[-1]]
        return num