# DP. Time O(n * k^2 + mk)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dict_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        max_len = max(map(len, wordDict))
        for i in range(1, n + 1):
            for j in range(i - 1, max(i - max_len - 1, -1), -1):
                if dp[j] and s[j:i] in dict_set:
                    dp[i] = True
                    break
        return dp[n]


# Another DP. Time O(nmk)
class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * n
        for i in range(n):
            for word in wordDict:
                if i < len(word) - 1:
                    continue
                if i == len(word) - 1 or dp[i - len(word)]:
                    if s[i - len(word) + 1 : i + 1] == word:
                        dp[i] = True
                        break
        return dp[-1]


# BFS. Time O(n^3 + mk)
class Solution3:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        queue = deque([0])
        visited = set()
        while queue:
            start = queue.popleft()
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if end not in visited and s[start: end] in words:
                    queue.append(end)
                    visited.add(end)
        return False