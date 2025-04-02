# Time O(n * n!) Space O(n * n!)
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        sequences = set()
        used = [False] * len(tiles)

        def backtrack(path):
            sequences.add(path)
            for i, c in enumerate(tiles):
                if not used[i]:
                    used[i] = True
                    backtrack(path + c)
                    used[i] = False

        backtrack("")
        return len(sequences) - 1


# Time O(n!) Space O(n)
class Solution2:
    def numTilePossibilities(self, tiles: str) -> int:
        cnt = [0] * 26
        res = 0
        for c in tiles:
            cnt[ord(c) - ord('A')] += 1

        def backtrack():
            nonlocal res
            for i in range(26):
                if cnt[i] == 0:
                    continue
                res += 1
                cnt[i] -= 1
                backtrack()
                cnt[i] += 1

        backtrack()
        return res