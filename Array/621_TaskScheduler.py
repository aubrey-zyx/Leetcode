class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        max_cnt = max(cnt.values())
        ans = (max_cnt - 1) * (n + 1)
        for val in cnt.values():
            if val == max_cnt:
                ans += 1
        return ans if ans >= len(tasks) else len(tasks)