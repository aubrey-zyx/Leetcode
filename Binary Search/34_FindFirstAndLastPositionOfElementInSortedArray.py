class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, target, is_searching_left):
            left, right = 0, len(nums) - 1
            idx = -1
            while left <= right:
                mid = left + (right - left) // 2
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    idx = mid
                    if is_searching_left:
                        right = mid - 1
                    else:
                        left = mid + 1
            return idx

        first = binary_search(nums, target, True)
        last = binary_search(nums, target, False)
        return [first, last]


class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect_left(nums, target)
        right = bisect_right(nums, target) - 1
        return [left, right] if left <= right < len(nums) else [-1, -1]


class Solution3:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, target, left):
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if left:
                    if target <= nums[mid]:
                        r = mid
                    else:
                        l = mid + 1
                else:
                    if target >= nums[mid]:
                        l = mid + 1
                    else:
                        r = mid
            return l

        first = binary_search(nums, target, True)
        last = binary_search(nums, target, False) - 1
        return [first, last] if first <= last < len(nums) else [-1, -1]