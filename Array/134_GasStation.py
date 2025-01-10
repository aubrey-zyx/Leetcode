class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gain = 0
        cur_gain = 0
        res = 0

        for i in range(len(gas)):
            total_gain += gas[i] - cost[i]
            cur_gain += gas[i] - cost[i]

            # If we meet a "valley", start over from the next station with 0 initial gas
            if cur_gain < 0:
                cur_gain = 0
                res = i + 1

        return res if total_gain >= 0 else -1


class Solution2:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gain = 0
        min_gain = float("inf")
        min_idx = 0
        for i in range(len(gas)):
            total_gain += gas[i] - cost[i]
            if total_gain < min_gain:
                min_gain = total_gain
                min_idx = i
        if total_gain < 0:
            return -1
        return (min_idx + 1) % len(gas)