#DFS
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        bipartite = True

        def dfs(node):
            nonlocal bipartite
            for nei in graph[node]:
                if nei not in color:
                    color[nei] = 1 - color[node]
                    dfs(nei)
                elif color[nei] == color[node]:
                    bipartite = False
                    return

        for node in range(len(graph)):
            if node not in color:
                color[node] = 0
                dfs(node)
                if not bipartite:
                    break

        return bipartite


#BFS
class Solution2:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        for i in range(len(graph)):
            if i not in color:
                queue = deque([i])
                color[i] = 0
                while queue:
                    node = queue.popleft()
                    for nei in graph[node]:
                        if nei not in color:
                            queue.append(nei)
                            color[nei] = 1 - color[node]
                        elif color[nei] == color[node]:
                            return False

        return True