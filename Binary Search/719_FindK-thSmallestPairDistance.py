class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count_smaller_distances(distance):  # <= distance
            count = 0
            l = 0
            for r in range(len(nums)):
                while nums[r] - nums[l] > distance:
                    l += 1
                count += r - l
            return count

        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left <= right:
            mid = (left + right) // 2
            if count_smaller_distances(mid) < k:
                left = mid + 1
            else:
                right = mid - 1
        return left