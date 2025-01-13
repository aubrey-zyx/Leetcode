# Two pointers and merge sort. O(m + n)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        i = j = 0

        def get_min():
            nonlocal i, j
            if i < m and j < n:
                if nums1[i] < nums2[j]:
                    ans = nums1[i]
                    i += 1
                else:
                    ans = nums2[j]
                    j += 1
            elif i == m:
                ans = nums2[j]
                j += 1
            else:
                ans = nums1[i]
                i += 1
            return ans

        if (m + n) % 2 == 0:
            for _ in range((m + n) // 2 - 1):
                get_min()
            return (get_min() + get_min()) / 2
        else:
            for _ in range((m + n) // 2):
                get_min()
            return get_min()


# Binary Search, O(log(m + n))
class Solution2:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        na, nb = len(A), len(B)
        n = na + nb

        def solve(k, a_start, a_end, b_start, b_end):
            if a_start > a_end:
                return B[k - a_start]
            if b_start > b_end:
                return A[k - b_start]

            a_idx, b_idx = (a_start + a_end) // 2, (b_start + b_end) // 2
            a_val, b_val = A[a_idx], B[b_idx]

            # If k is in the right half of A + B, remove the smaller left half
            if k > a_idx + b_idx:
                if a_val < b_val:
                    return solve(k, a_idx + 1, a_end, b_start, b_end)
                else:
                    return solve(k, a_start, a_end, b_idx + 1, b_end)
            # Otherwise, remove the larger right half
            else:
                if a_val > b_val:
                    return solve(k, a_start, a_idx - 1, b_start, b_end)
                else:
                    return solve(k, a_start, a_end, b_start, b_idx - 1)

        if n % 2:
            return solve(n // 2, 0, na - 1, 0, nb - 1)
        else:
            return (solve(n // 2 - 1, 0, na - 1, 0, nb - 1) + solve(n // 2, 0, na - 1, 0, nb - 1)) / 2