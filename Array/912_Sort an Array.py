# Merge Sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            res = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            res.extend(left[i:])
            res.extend(right[j:])
            return res

        def merge_sort(nums):
            n = len(nums)
            if n <= 1:
                return nums
            mid = n // 2
            sorted_left = merge_sort(nums[:mid])
            sorted_right = merge_sort(nums[mid:])
            return merge(sorted_left, sorted_right)

        return merge_sort(nums)


# Heap Sort
class Solution2:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and nums[left] > nums[largest]:
                largest = left
            if right < n and nums[right] > nums[largest]:
                largest = right
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(n, largest)

        def heap_sort():
            n = len(nums)
            for i in range(n // 2 - 1, -1, -1):
                heapify(n, i)
            for i in range(n - 1, -1, -1):
                nums[0], nums[i] = nums[i], nums[0]
                heapify(i, 0)

        heap_sort()
        return nums