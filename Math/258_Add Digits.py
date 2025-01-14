class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            sum = 0
            while num:
                sum += num % 10
                num //= 10
            num = sum
        return num


class Solution2:
    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0