class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        adjacent = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    adjacent[i].append(j)
                    adjacent[j].append(i)

        groups = 0
        visited = [False] * n

        def dfs(stone):
            visited[stone] = True
            for nei in adjacent[stone]:
                if not visited[nei]:
                    dfs(nei)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                groups += 1
        return n - groups


class Solution2:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    uf.union(i, j)
        return n - uf.groups


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.groups = n

    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        elif self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[px] = py
            self.rank[py] += 1
        self.groups -= 1