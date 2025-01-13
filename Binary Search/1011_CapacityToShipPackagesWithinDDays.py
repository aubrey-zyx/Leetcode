class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        left, right = max(max(weights), math.ceil(sum(weights) / days)), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            day_count, cur = 1, 0
            for weight in weights:
                if cur + weight > mid:
                    day_count += 1
                    cur = 0
                cur += weight
            if day_count <= days:
                right = mid
            else:
                left = mid + 1
        return left