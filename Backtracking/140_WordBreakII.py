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
        word_set = set(wordDict)
        n = len(s)

        def backtrack(start, cur):
            if start == n:
                res.append(" ".join(cur))
                return
            for end in range(start + 1, n + 1):
                word = s[start: end]
                if word in word_set:
                    cur.append(word)
                    backtrack(end, cur)
                    cur.pop()

        backtrack(0, [])
        return res