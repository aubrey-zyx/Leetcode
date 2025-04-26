# DFS - Brute Force. O(n^2)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def dfs(source, target):
            if source in seen:
                return
            if source == target:
                return True
            seen.add(source)
            for nei in graph[source]:
                if dfs(nei, target):
                    return True
            return False

        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v):
                return [u, v]
            graph[u].append(v)
            graph[v].append(u)


# DFS - Single Traversal. O(n)
class Solution2:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        visited = [False] * (n + 1)
        parent = [-1] * (n + 1)

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        cycle_start = -1
        cycle = set()

        def dfs(node):
            nonlocal cycle_start
            visited[node] = True
            for nei in adj[node]:
                if not visited[nei]:
                    parent[nei] = node
                    dfs(nei)
                elif nei != parent[node] and cycle_start == -1:
                    cycle_start = nei
                    parent[nei] = node

        dfs(1)

        cur = cycle_start
        while True:
            cycle.add(cur)
            cur = parent[cur]
            if cur == cycle_start:
                break

        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
        return []


# Union-Find
class Solution3:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        rank = [0] * (n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[px] = py
                rank[py] += 1

        for u, v in edges:
            if find(u) != find(v):
                union(u, v)
            else:
                return [u, v]

        return []