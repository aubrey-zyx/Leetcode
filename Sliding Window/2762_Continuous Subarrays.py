class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        res = 0
        l = r = 0
        subarray = sortedcontainers.SortedList()
        while r < len(nums):
            subarray.add(nums[r])
            while subarray[-1] - subarray[0] > 2:
                subarray.remove(nums[l])
                l += 1
            res += r - l + 1
            r += 1

        return res


class Solution2:
    def continuousSubarrays(self, nums: List[int]) -> int:
        res = 0
        l = r = 0
        freq = defaultdict(int)
        while r < len(nums):
            freq[nums[r]] += 1
            while max(freq) - min(freq) > 2:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1
            res += r - l + 1
            r += 1

        return res


class Solution3:
    def continuousSubarrays(self, nums: List[int]) -> int:
        res = 0
        l = 0
        min_q = deque()
        max_q = deque()

        for r, num in enumerate(nums):
            while max_q and num > nums[max_q[-1]]:
                max_q.pop()
            max_q.append(r)

            while min_q and num < nums[min_q[-1]]:
                min_q.pop()
            min_q.append(r)

            while nums[max_q[0]] - nums[min_q[0]] > 2:
                if max_q[0] < min_q[0]:
                    l = max_q[0] + 1
                    max_q.popleft()
                else:
                    l = min_q[0] + 1
                    min_q.popleft()

            res += r - l + 1

        return res