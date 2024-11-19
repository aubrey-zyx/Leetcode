class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotated = []
        for c in reversed(num):
            if c in {'0', '1', '8'}:
                rotated.append(c)
            elif c == '6':
                rotated.append('9')
            elif c == '9':
                rotated.append('6')
            else:
                return False
        return "".join(rotated) == num


# Two pointers
class Solution2:
    def isStrobogrammatic(self, num: str) -> bool:
        mp = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        l, r = 0, len(num) - 1
        while l <= r:
            if num[l] not in mp or num[r] not in mp or mp[num[l]] != num[r]:
                return False
            l += 1
            r -= 1
        return True