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