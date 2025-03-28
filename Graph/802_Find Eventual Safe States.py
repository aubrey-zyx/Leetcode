class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        outdegree = [0] * n
        reversed_adj = [[] for _ in range(n)]
        for u in range(n):
            for v in graph[u]:
                reversed_adj[v].append(u)
                outdegree[u] += 1

        queue = deque()
        for i in range(n):
            if outdegree[i] == 0:
                queue.append(i)

        safe = [False] * n
        while queue:
            node = queue.popleft()
            safe[node] = True
            for nei in reversed_adj[node]:
                outdegree[nei] -= 1
                if outdegree[nei] == 0:
                    queue.append(nei)

        res = []
        for i in range(n):
            if safe[i]:
                res.append(i)
        return res