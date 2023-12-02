class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0] * (n - 1) + [-1]
        right_max = -1
        for i in range(n - 2, -1, -1):
            right_max = max(right_max, arr[i + 1])
            res[i] = right_max
        return res