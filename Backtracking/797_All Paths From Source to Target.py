class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        target = len(graph) - 1

        def backtrack(node, path):
            if node == target:
                res.append(path.copy())
                return
            for neighbor in graph[node]:
                path.append(neighbor)
                backtrack(neighbor, path)
                path.pop()

        backtrack(0, [0])
        return res