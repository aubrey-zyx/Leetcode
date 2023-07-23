class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []    # pair: [temp, index]
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                pop_t, pop_idx = stack.pop()
                ans[pop_idx] = i - pop_idx
            stack.append((t, i))
        return ans