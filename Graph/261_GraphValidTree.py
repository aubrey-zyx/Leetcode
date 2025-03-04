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