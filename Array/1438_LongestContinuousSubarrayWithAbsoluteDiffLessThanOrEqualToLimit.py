from sortedcontainers import SortedList

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        res = 0
        subarray = SortedList()
        l = r = 0
        while r < n:
            subarray.add(nums[r])
            while subarray[-1] - subarray[0] > limit:
                subarray.remove(nums[l])
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res


# Monotonic queues
class Solution2:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0
        dec_queue = collections.deque()
        inc_queue = collections.deque()
        l = 0

        for r, num in enumerate(nums):
            while dec_queue and num > dec_queue[-1]:
                dec_queue.pop()
            dec_queue.append(num)

            while inc_queue and num < inc_queue[-1]:
                inc_queue.pop()
            inc_queue.append(num)

            while dec_queue[0] - inc_queue[0] > limit:
                if nums[l] == dec_queue[0]:
                    dec_queue.popleft()
                if nums[l] == inc_queue[0]:
                    inc_queue.popleft()
                l += 1

            res = max(res, r - l + 1)

        return res