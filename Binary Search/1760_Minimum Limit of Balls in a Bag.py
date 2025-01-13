class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def is_possible(penalty):
            total_operations = 0
            for num in nums:
                operations = math.ceil(num / penalty) - 1
                total_operations += operations
                if total_operations > maxOperations:
                    return False
            return True

        l, r = 1, max(nums)
        while l < r:
            mid = l + (r - l) // 2
            if is_possible(mid):
                r = mid
            else:
                l = mid + 1
        return l