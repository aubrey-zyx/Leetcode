from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = 0
        while i < n:
            sum_of_gas = sum_of_cost = 0
            count = 0
            while count < n:
                j = (i + count) % n
                sum_of_gas += gas[j]
                sum_of_cost += cost[j]
                if sum_of_gas < sum_of_cost:
                    break
                count += 1
            if count == n:
                return i
            else:
                i += count + 1
        return -1


class Solution2:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        spare = 0    # total spare gas
        min_spare = float("inf")    # minimum spare gas
        min_index = 0    # station with minimum spare gas
        for i in range(n):
            spare += gas[i] - cost[i]
            if spare < min_spare:
                min_spare = spare
                min_index = i
        if spare < 0:
            return -1
        elif min_spare >= 0:    # means that the circuit can be completed starting from whichever station
            return 0
        else:
            return (min_index + 1) % n    # the starting position should be the next to min_index