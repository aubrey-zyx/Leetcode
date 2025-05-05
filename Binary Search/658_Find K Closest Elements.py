class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        right = bisect_left(arr, x)
        left = right - 1
        for _ in range(k):
            if left < 0:
                right += 1
            elif right >= len(arr) or x - arr[left] <= arr[right] - x:
                left -= 1
            else:
                right += 1
        return arr[left + 1: right]


class Solution2:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def bl(arr, x):
            l, r = 0, len(arr)
            while l < r:
                m = (l + r) // 2
                if x <= arr[m]:
                    r = m
                else:
                    l = m + 1
            return l

        right = bl(arr, x)
        left = right - 1
        for _ in range(k):
            if left < 0:
                right += 1
            elif right >= len(arr) or x - arr[left] <= arr[right] - x:
                left -= 1
            else:
                right += 1
        return arr[left + 1: right]