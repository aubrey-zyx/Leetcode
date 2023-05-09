class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev = self.countAndSay(n-1)
        res = ""
        i = 0
        for j, ch in enumerate(prev):
            if ch != prev[i]:
                res += str(j-i) + prev[i]
                i = j
        res += str(len(prev) - i) + prev[-1]
        return res


'''
*************Iteration method**************
class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for i in range(1, n):
            curr = ""
            j = 0
            while j < len(res):
                count = 1
                while j+1 < len(res) and res[j] == res[j+1]:
                    count += 1
                    j += 1
                curr += str(count) + res[j]
                j += 1
            res = curr
        return res
'''