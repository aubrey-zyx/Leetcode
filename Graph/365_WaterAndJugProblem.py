class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target > x + y:
            return False

        queue = deque([(0, 0)])
        visited = set((0, 0))
        while queue:
            a, b = queue.popleft()
            if a + b == target:
                return True

            states = set()
            states.add((x, b))  # Fill jar x
            states.add((a, y))  # Fill jar y
            states.add((0, y))  # Empty jar x
            states.add((a, 0))  # Empty jar y
            states.add((0 if y >= b + a else a - (y - b), min(b + a, y)))  # Pour jar x to y
            states.add((min(x, a + b), 0 if x >= a + b else b - (x - a)))  # Pour jar y to x

            for state in states:
                if state in visited:
                    continue
                queue.append(state)
                visited.add(state)

        return False


class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target > x + y:
            return False

        visited = set()

        def dfs(a, b):
            if a + b == target:
                return True

            if (a, b) in visited:
                return False

            visited.add((a, b))

            fill_a = dfs(x, b)
            fill_b = dfs(a, y)
            empty_a = dfs(0, b)
            empty_b = dfs(a, 0)
            pour_a = dfs(max(0, a - (y - b)), min(b + a, y))
            pour_b = dfs(min(a + b, x), max(0, b - (x - a)))

            return fill_a or fill_b or empty_a or empty_b or pour_a or pour_b

        return dfs(0, 0)