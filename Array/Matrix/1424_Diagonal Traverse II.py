class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        for r in range(len(nums) - 1, -1, -1):
            for c in range(len(nums[r])):
                d = r + c
                diagonals[d].append(nums[r][c])
        res = []
        d = 0
        while d in diagonals:
            res.extend(diagonals[d])
            d += 1
        return res
    

# BFS
class Solution2:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        queue = deque([(0, 0)])
        while queue:
            r, c = queue.popleft()
            res.append(nums[r][c])
            if c == 0 and r < len(nums) - 1:
                queue.append((r + 1, c))
            if c < len(nums[r]) - 1:
                queue.append((r, c + 1))
        return res