class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(defaultdict)

        def backtrack(start, target, product, visited):
            visited.add(start)
            res = -1.0
            neighbors = graph[start]
            for neighbor, value in neighbors.items():
                if neighbor == target:
                    return product * neighbors[target]
                if neighbor in visited:
                    continue
                res = backtrack(neighbor, target, product * value, visited)
                if res != -1.0:
                    break
            visited.remove(start)
            return res

        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        res = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                res.append(-1.0)
            elif dividend == divisor:
                res.append(1.0)
            else:
                res.append(backtrack(dividend, divisor, 1, set()))
        return res