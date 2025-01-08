class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        return x == x[::-1]


# Without converting the integer to a string
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        reverted_num = 0
        while x > reverted_num:
            reverted_num = reverted_num * 10 + x % 10
            x //= 10
        return x == reverted_num or x == reverted_num // 10
