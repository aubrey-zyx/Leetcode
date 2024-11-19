class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        res = 0
        l = 0
        equal = 0
        for r in range(len(ages)):
            while l < r and ages[l] <= 0.5 * ages[r] + 7:
                l += 1
            while ages[equal] != ages[r]:
                equal += 1
            res += r - l
            res += r - max(l, equal)
        return res