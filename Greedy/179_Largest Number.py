class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def sort_rule(a, b):
            x, y = a + b, b + a
            if x > y:
                return 1
            elif x < y:
                return -1
            else:
                return 0

        strs = [str(num) for num in nums]
        strs.sort(key=functools.cmp_to_key(sort_rule), reverse=True)
        if strs[0] == "0":
            return "0"
        return "".join(strs)