class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        res = 0
        n = len(s)
        i = 0
        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)

        while i < n and s[i] == " ":
            i += 1

        if i < n:
            if s[i] == "+":
                sign = 1
                i += 1
            elif s[i] == "-":
                sign = -1
                i += 1

        while i < n and s[i].isdigit():
            digit = int(s[i])
            if (res > INT_MAX // 10) or (
                    res == INT_MAX // 10 and digit > INT_MAX % 10
            ):
                return INT_MAX if sign == 1 else INT_MIN
            res = res * 10 + digit
            i += 1

        return sign * res