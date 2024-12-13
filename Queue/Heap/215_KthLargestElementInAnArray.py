class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]


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