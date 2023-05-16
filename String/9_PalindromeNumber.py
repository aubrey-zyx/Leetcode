class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        return x == x[::-1]


'''   
***********Without converting the integer to a string*************8
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x = x // 10
        if x == rev or x == rev // 10:
            return True
        else:
            return False
'''