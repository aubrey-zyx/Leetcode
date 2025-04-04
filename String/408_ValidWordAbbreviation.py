class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        m, n = len(word), len(abbr)
        i = j = 0
        while j < n and i < m:
            if abbr[j] == "0":
                return False
            elif word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isnumeric():
                k = j
                while k < n and abbr[k].isnumeric():
                    k += 1
                i += int(abbr[j:k])
                j = k
            else:
                return False
        return i == m and j == n