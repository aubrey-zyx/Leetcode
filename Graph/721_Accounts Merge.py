# DFS: build adjacency list first
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj = defaultdict(list)
        visited = set()
        email_to_name = {}

        for account in accounts:
            emails = account[1:]
            first = emails[0]
            for email in emails:
                adj[first].append(email)
                adj[email].append(first)
                email_to_name[email] = account[0]

        def dfs(node, component):
            if node in visited:
                return
            visited.add(node)
            component.append(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei, component)

        res = []
        for email, name in email_to_name.items():
            if email in visited:
                continue
            component = []
            dfs(email, component)
            res.append([name] + sorted(component))
        return res


# DFS
class Solution2:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_idx = defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_to_idx[email].append(i)

        def dfs(i, component):
            visited[i] = True
            for email in accounts[i][1:]:
                if email in component:
                    continue
                component.append(email)
                for j in email_to_idx[email]:
                    if not visited[j]:
                        dfs(j, component)

        res = []
        n = len(accounts)
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                component = []
                dfs(i, component)
                res.append([accounts[i][0]] + sorted(component))
        return res


# Union Find
class Solution3:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        email_to_idx = {}

        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in email_to_idx:
                    uf.union(i, email_to_idx[email])
                else:
                    email_to_idx[email] = i

        group = defaultdict(list)
        for email, i in email_to_idx.items():
            group[uf.find(i)].append(email)

        return [[accounts[i][0]] + sorted(emails) for i, emails in group.items()]


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[px] = py
            self.rank[py] += 1