class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        for log in logs:
            func, status, time = log.split(":")
            func, time = int(func), int(time)
            if status == "start":
                if stack:
                    res[stack[-1][0]] += time - stack[-1][1]
                    stack[-1][1] = time
                stack.append([func, time])
            else:
                i, start = stack.pop()
                res[i] += time - start + 1
                if stack:
                    stack[-1][1] = time + 1
        return res