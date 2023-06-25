from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0
        ans = 0
        left = 0
        while left < n - 2:
            right = left + 1
            if arr[left] < arr[left + 1]:
                while right + 1 < n and arr[right] < arr[right + 1]:
                    right += 1
                if right < n - 1 and arr[right] > arr[right + 1]:
                    while right + 1 < n and arr[right] > arr[right + 1]:
                        right += 1
                    ans = max(ans, right - left + 1)
                else:
                    right += 1
            left = right
        return ans


class Solution2:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        i = 1
        while i < n - 1:
            peak = arr[i] > arr[i - 1] and arr[i] > arr[i + 1]
            if not peak:
                i += 1
                continue

            left = i - 1
            while left > 0 and arr[left - 1] < arr[left]:
                left -= 1

            right = i + 1
            while right < n - 1 and arr[right] > arr[right + 1]:
                right += 1

            ans = max(ans, right - left + 1)
            i = right + 1
        return ans