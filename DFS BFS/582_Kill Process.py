class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        children = defaultdict(list)
        for i in range(len(ppid)):
            children[ppid[i]].append(pid[i])

        queue = deque([kill])
        res = []
        while queue:
            cur = queue.popleft()
            res.append(cur)
            for child in children[cur]:
                queue.append(child)

        return res


class Solution2:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        children = defaultdict(list)
        for i in range(len(ppid)):
            children[ppid[i]].append(pid[i])

        def dfs(p):
            res = [p]
            for child in children[p]:
                res.extend(dfs(child))
            return res

        return dfs(kill)