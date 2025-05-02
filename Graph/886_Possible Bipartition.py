# BFS
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u, v in dislikes:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(source):
            queue = deque([source])
            color[source] = 0
            while queue:
                node = queue.popleft()
                for nei in adj[node]:
                    if color[nei] == color[node]:
                        return False
                    if color[nei] == -1:
                        color[nei] = 1 - color[node]
                        queue.append(nei)
            return True

        color = [-1] * (n + 1)
        for i in range(1, n + 1):
            if color[i] == -1:
                if not bfs(i):
                    return False
        return True


# DFS
class Solution2:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u, v in dislikes:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, node_color):
            color[node] = node_color
            for nei in adj[node]:
                if color[nei] == color[node]:
                    return False
                if color[nei] == -1:
                    if not dfs(nei, 1 - node_color):
                        return False
            return True

        color = [-1] * (n + 1)
        for i in range(1, n + 1):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
        return True


# Union Find
class Solution3:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u, v in dislikes:
            adj[u].append(v)
            adj[v].append(u)

        uf = UnionFind(n + 1)
        for node in range(1, n + 1):
            for nei in adj[node]:
                if uf.find(node) == uf.find(nei):
                    return False
                uf.union(adj[node][0], nei)
        return True


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

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