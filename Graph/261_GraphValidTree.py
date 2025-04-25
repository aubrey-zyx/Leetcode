# BFS
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacent = defaultdict(list)
        for n1, n2 in edges:
            adjacent[n1].append(n2)
            adjacent[n2].append(n1)

        queue = deque([0])
        visited = set([0])
        parent = {}
        while queue:
            node = queue.popleft()
            for nei in adjacent[node]:
                if parent.get(node) == nei:
                    continue
                if nei in visited:
                    return False
                parent[nei] = node
                queue.append(nei)
                visited.add(nei)
        return len(visited) == n


# DFS
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacent = defaultdict(list)
        for n1, n2 in edges:
            adjacent[n1].append(n2)
            adjacent[n2].append(n1)

        visited = set()

        def dfs(i, prev):
            if i in visited:
                return False
            visited.add(i)
            for j in adjacent[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n


# Advanced Graph Theory + Iterative DFS
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # For the graph to be a valid tree, it must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = {0}
        stack = [0]

        while stack:
            node = stack.pop()
            for nei in adj[node]:
                if nei in visited:
                    continue
                visited.add(nei)
                stack.append(nei)

        return len(visited) == n