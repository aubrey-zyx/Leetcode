class Solution:
    def get_digit_sum(self, num):
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        return digit_sum

    def maximumSum(self, nums: List[int]) -> int:
        heaps = defaultdict(list)
        res = -1

        for num in nums:
            digit_sum = self.get_digit_sum(num)
            heapq.heappush(heaps[digit_sum], num)
            if len(heaps[digit_sum]) > 2:
                heapq.heappop(heaps[digit_sum])

        for heap in heaps.values():
            if len(heap) == 2:
                res = max(res, heap[0] + heap[1])

        return res