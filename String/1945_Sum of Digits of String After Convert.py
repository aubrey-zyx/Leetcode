class Solution:
    def getLucky(self, s: str, k: int) -> int:
        converted = ""
        for c in s:
            converted += str(ord(c) - ord('a') + 1)
        for _ in range(k):
            digit_sum = 0
            for digit in converted:
                digit_sum += int(digit)
            if digit_sum < 10:
                return digit_sum
            converted = str(digit_sum)
        return int(converted)


# O(1) space
class Solution2:
    def getLucky(self, s: str, k: int) -> int:
        num = 0
        for c in s:
            pos = ord(c) - ord('a') + 1
            while pos > 0:
                num += pos % 10
                pos //= 10
        for i in range(k - 1):
            new_num = 0
            while num > 0:
                new_num += num % 10
                num //= 10
            num = new_num
            if num < 10:
                break
        return num