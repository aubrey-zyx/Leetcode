# BFS
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set([source])
        queue = deque([source])

        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)

        return False


# DFS
class Solution2:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            if node == destination:
                return True
            if node not in visited:
                visited.add(node)
                for nei in graph[node]:
                    if dfs(nei):
                        return True
            return False

        return dfs(source)
    

class Solution3:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)
        return uf.find(source) == uf.find(destination)

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