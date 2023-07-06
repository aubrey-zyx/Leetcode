class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        ht = {}
        for i, num in enumerate(nums):
            if num in ht:
                ht[num][0] += 1    # The first element represents frequency
                ht[num][2] = i    # The third element represents the last occurence position
            else:
                ht[num] = [1, i, i]    # The second element represents the first occurence position
        degree = 1
        ans = len(nums)
        for count, left, right in ht.values():
            if degree < count:
                degree = count
                ans = right - left + 1
            elif degree == count:
                ans = min(ans, right - left + 1)
        return ans