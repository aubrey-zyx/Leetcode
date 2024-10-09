class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        for i in range(min(m, n), 0, -1):
            if m % i == 0 and n % i == 0:
                candidate = str1[: i]
                if candidate * (m // i) == str1 and candidate * (n // i) == str2:
                    return candidate
        return ""


class Solution2:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        return str1[: math.gcd(len(str1), len(str2))]