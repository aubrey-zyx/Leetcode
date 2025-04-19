class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        d = dict(replacements)

        def dfs(text):
            i = 0
            res = []

            while i < len(text):
                if text[i] == "%":
                    key = text[i + 1]
                    res.append(dfs(d[key]))
                    i += 3
                else:
                    res.append(text[i])
                    i += 1

            return "".join(res)

        return dfs(text)