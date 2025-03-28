class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        equal = []
        greater = []
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)
        return less + equal + greater


class Solution2:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = 0
        equal = 0
        for num in nums:
            if num < pivot:
                less += 1
            elif num == pivot:
                equal += 1

        res = [0] * len(nums)
        i, j, k = 0, less, less + equal
        for num in nums:
            if num < pivot:
                res[i] = num
                i += 1
            elif num == pivot:
                res[j] = num
                j += 1
            else:
                res[k] = num
                k += 1
        return res


# Two pointer
class Solution3:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        res = [0] * n
        less_i, greater_i = 0, n - 1

        for i, j in zip(range(n), range(n - 1, -1, -1)):
            if nums[i] < pivot:
                res[less_i] = nums[i]
                less_i += 1
            if nums[j] > pivot:
                res[greater_i] = nums[j]
                greater_i -= 1

        while less_i <= greater_i:
            res[less_i] = pivot
            less_i += 1

        return res