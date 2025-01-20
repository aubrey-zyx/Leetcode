class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n

        balls_left = moves_left = 0
        balls_right = moves_right = 0

        for i in range(n):
            res[i] += moves_left
            balls_left += int(boxes[i])
            moves_left += balls_left

            j = n - 1 - i
            res[j] += moves_right
            balls_right += int(boxes[j])
            moves_right += balls_right

        return res