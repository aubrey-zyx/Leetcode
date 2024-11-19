class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = Trie()
        res = []
        for word in sorted(words, key=len):
            if word == "":
                continue
            if trie.search(word):
                res.append(word)
            else:
                trie.insert(word)
        return res


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        cur = self.root
        for c in word + "#":
            if c not in cur:
                cur[c] = {}
            cur = cur[c]

    def search(self, word):
        cur = self.root
        for i in range(len(word)):
            if "#" in cur:
                if self.search(word[i:]):
                    return True
            if word[i] in cur:
                cur = cur[word[i]]
            else:
                return False
        return "#" in cur


# DFS BFS & Memorization Search
class Solution2:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)
        dp = {}

        def dfs(word):
            if word in dp:
                return dp[word]

            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if ((prefix in wordSet and suffix in wordSet) or
                        (prefix in wordSet and dfs(suffix))):
                    dp[word] = True
                    return True
            dp[word] = False
            return False

        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        return res