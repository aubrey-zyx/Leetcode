class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        threshold *= k
        n = len(arr)
        if k > n:
            return 0
        cur_sum = sum(arr[:k])
        if cur_sum >= threshold:
            count += 1
        for r in range(k, n):
            cur_sum = cur_sum + arr[r] - arr[r - k]
            if cur_sum >= threshold:
                count += 1
        return count