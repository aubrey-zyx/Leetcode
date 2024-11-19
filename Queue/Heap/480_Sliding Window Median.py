from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = []
        win = SortedList([])
        for i in range(len(nums)):
            if i >= k:
                win.remove(nums[i - k])
            win.add(nums[i])
            if i >= k - 1:
                median = win[k // 2] if k % 2 == 1 else (win[k // 2 - 1] + win[k // 2]) / 2
                res.append(median)
        return res


class Solution2:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = []
        low, high = [], []
        mp = defaultdict(int)
        n = len(nums)

        for i in range(k):
            heappush(low, -nums[i])
        for j in range(k // 2):
            heappush(high, -heappop(low))

        if k % 2 == 1:
            res.append(-low[0])
        else:
            res.append((high[0] - low[0]) / 2)

        balance = 0  # Number of valid nums in low - Number of valid nums in high
        for i in range(1, n - k + 1):
            out_num = nums[i - 1]
            mp[out_num] += 1
            if out_num <= (-low[0]):
                balance -= 1
            else:
                balance += 1

            in_num = nums[i + k - 1]
            if in_num <= (-low[0]):
                heappush(low, -in_num)
                balance += 1
            else:
                heappush(high, in_num)
                balance -= 1

            # Now balance could be 0/2/-2. Make two heaps balance again
            if balance > 0:
                heappush(high, -heappop(low))
            if balance < 0:
                heappush(low, -heappop(high))
            balance = 0

            # Remove invalid numbers when they are at heap tops (Lazy Removal)
            while low and mp[-low[0]] > 0:
                mp[-low[0]] -= 1
                heappop(low)
            while high and mp[high[0]] > 0:
                mp[high[0]] -= 1
                heappop(high)

            if k % 2 == 1:
                res.append(-low[0])
            else:
                res.append((high[0] - low[0]) / 2)

        return res