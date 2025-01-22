class Solution:
    def minSwaps(self, data: List[int]) -> int:
        win_len = sum(data)
        ones = 0
        max_ones = 0
        for r in range(len(data)):
            ones += data[r]
            if r >= win_len:
                ones -= data[r - win_len]
            max_ones = max(max_ones, ones)
        return win_len - max_ones