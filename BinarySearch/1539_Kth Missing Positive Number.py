class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for num in arr:
            if num <= k:
                k += 1
            else:
                break
        return k


class Solution2:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        cur = 1
        i = 0
        res = -1
        while k > 0:
            if cur == arr[i]:
                if i < len(arr) - 1:
                    i += 1
            else:
                k -= 1
                res = cur
            cur += 1
        return res


# Binary Search
class Solution3:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m] - m - 1 < k:
                l = m + 1
            else:
                r = m - 1

        # At the end of the loop, l = r + 1
        # The kth missing is in-between arr[r] and arr[l]
        # arr[r] + k - (arr[r] - r - 1) = k + l
        return l + k


