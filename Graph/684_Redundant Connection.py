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


# Union-Find
class Solution2:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for u, v in edges:
            if find(u) != find(v):
                union(u, v)
            else:
                return [u, v]

        return []