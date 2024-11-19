class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]


# Quick Select
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []

            for num in nums:
                if num < pivot:
                    right.append(num)
                elif num > pivot:
                    left.append(num)
                else:
                    mid.append(num)

            if k <= len(left):
                return quick_select(left, k)
            if k > len(left) + len(mid):
                return quick_select(right, k - len(left) - len(mid))
            return pivot

        return quick_select(nums, k)