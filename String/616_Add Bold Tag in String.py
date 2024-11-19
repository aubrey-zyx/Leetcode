class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        n = len(s)
        bold = [False] * n

        for word in words:
            start = s.find(word)
            while start != -1:
                for i in range(start, start + len(word)):
                    bold[i] = True
                start = s.find(word, start + 1)

        res = []
        for i in range(n):
            if bold[i] and (i == 0 or not bold[i - 1]):
                res.append("<b>")
            res.append(s[i])
            if bold[i] and (i == n - 1 or not bold[i + 1]):
                res.append("</b>")

        return "".join(res)