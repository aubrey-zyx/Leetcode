class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums = set(nums)

        def backtrack(cur):
            if len(cur) == n:
                if cur not in nums:
                    return cur
                return ""
            add_zero = backtrack(cur + "0")
            return add_zero if add_zero else backtrack(cur + "1")

        return backtrack("")


class Solution2:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        integers = set()
        for num in nums:
            integers.add(int(num, 2))

        n = len(nums)
        for num in range(n + 1):
            if num not in integers:
                res = bin(num)[2:]
                return "0" * (n - len(res)) + res