class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        left_max = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max = [0] * (n - 1) + [height[-1]]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        res = sum(min(left_max[i], right_max[i]) - height[i] for i in range(n))
        return res


# Two pointers
class Solution2:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        left_max, right_max = height[0], height[-1]
        res = 0

        while l < r:
            if height[l] < height[r]:
                left_max = max(left_max, height[l])
                res += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                res += right_max - height[r]
                r -= 1
        return res


# Monotonic stack
class Solution3:
    def trap(self, height: List[int]) -> int:
        res = 0
        stack = []

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                cur_width = i - left - 1
                cur_height = min(height[left], height[i]) - height[top]
                res += cur_width * cur_height
            stack.append(i)

        return res