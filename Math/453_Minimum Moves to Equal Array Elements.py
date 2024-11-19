class Solution:
    def minMoves(self, nums: List[int]) -> int:
        moves = 0
        min_num = float("inf")
        for num in nums:
            moves += num
            min_num = min(min_num, num)
        return moves - min_num * len(nums)