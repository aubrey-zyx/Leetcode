class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        dict_set = set(wordDict)
        n = len(s)

        def backtrack(left, words):
            if left == n:
                res.append(" ".join(words))
                return
            for word in dict_set:
                if s[left:].startswith(word):
                    words.append(word)
                    backtrack(left + len(word), words)
                    words.pop()

        backtrack(0, [])
        return res


class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []

        def dfs(i, path):
            if i == len(s):
                res.append(" ".join(path))
                return
            for word in wordDict:
                if s[i:].startswith(word):
                    dfs(i + len(word), path + [word])

        dfs(0, [])
        return res