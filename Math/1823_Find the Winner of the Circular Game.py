class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque(range(1, n + 1))
        while len(queue) > 1:
            for _ in range(k - 1):
                queue.append(queue.popleft())
            queue.popleft()
        return queue[0]


# Math + Recursion
class Solution2:
    def findTheWinner(self, n: int, k: int) -> int:
        def helper(n, k):
            if n == 1:
                return 0
            return (helper(n - 1, k) + k) % n

        return helper(n, k) + 1