class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        d = {}
        for x, y in pairs:
            d[x] = set(preferences[x][:preferences[x].index(y)])
            d[y] = set(preferences[y][:preferences[y].index(x)])
        res = 0
        for x in d:
            for u in d[x]:
                if x in d[u]:
                    res += 1
                    break
        return res