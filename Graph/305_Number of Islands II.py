class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        res = []
        uf = UnionFind(m * n)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r, c in positions:
            pos = r * n + c
            uf.add_island(pos)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                nei = nr * n + nc
                if 0 <= nr < m and 0 <= nc < n and uf.parent[nei] >= 0:
                    uf.union(pos, nei)
            res.append(uf.groups)

        return res


class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.rank = [0] * n
        self.groups = 0

    def add_island(self, x):
        if self.parent[x] >= 0:
            return
        self.parent[x] = x
        self.groups += 1

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[px] = py
            self.rank[py] += 1
        self.groups -= 1