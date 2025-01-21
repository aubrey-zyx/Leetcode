class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def get_neighbors(code):
            for i in range(4):
                x = code[i]
                next_x = "0" if x == "9" else str(int(x) + 1)
                yield code[:i] + next_x + code[i + 1:]
                prev_x = "9" if x == "0" else str(int(x) - 1)
                yield code[:i] + prev_x + code[i + 1:]

        visited = set(deadends)
        if "0000" in visited:
            return -1
        visited.add("0000")
        queue = deque(["0000"])
        turns = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == target:
                    return turns
                for nei in get_neighbors(cur):
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
            turns += 1
        return -1