class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(list('aeiouAEIOU'))
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] not in vowels:
                i += 1
                continue
            if s[j] not in vowels:
                j -= 1
                continue
            s[i] , s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ''.join(s)