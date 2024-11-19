class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        for i in range(len(heights) - 1, -1, -1):
            if not stack or heights[i] > heights[stack[-1]]:
                stack.append(i)
        return stack[::-1]