class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        res = ""
        carry = 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry, val = divmod(tmp, 10)
            res = str(val) + res
            i -= 1
            j -= 1
        return "1" + res if carry != 0 else res