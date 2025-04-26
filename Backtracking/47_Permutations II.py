class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        cnt = Counter(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for num in cnt:
                if cnt[num] > 0:
                    path.append(num)
                    cnt[num] -= 1
                    backtrack(path)
                    path.pop()
                    cnt[num] += 1

        backtrack([])
        return res


# Sort
class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        used = [False] * n

        def backtrack(path):
            if len(path) == n:
                res.append(path.copy())
                return

            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                path.append(nums[i])
                used[i] = True
                backtrack(path)
                path.pop()
                used[i] = False

        nums.sort()
        backtrack([])
        return res