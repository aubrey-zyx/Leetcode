class Solution:
    def can_partition(self, str_num, target):
        if not str_num and target == 0:
            return True

        for i in range(len(str_num)):
            left = str_num[:i + 1]
            right = str_num[i + 1:]
            if self.can_partition(right, target - int(left)):
                return True

        return False

    def punishmentNumber(self, n: int) -> int:
        res = 0
        for num in range(1, n + 1):
            square = num * num
            if self.can_partition(str(square), num):
                res += square
        return res