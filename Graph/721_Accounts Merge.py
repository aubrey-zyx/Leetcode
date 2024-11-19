class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        visited = {}
        email_to_account = {}

        for account in accounts:
            emails = account[1:]
            first_email = emails[0]
            for email in emails:
                graph[email].append(first_email)
                graph[first_email].append(email)
                visited[email] = False
                email_to_account[email] = account[0]

        def dfs(node, component):
            nonlocal visited, graph
            if visited[node]:
                return
            visited[node] = True
            component.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, component)

        res = []
        for email, account in email_to_account.items():
            if visited[email]:
                continue
            nodes = []
            dfs(email, nodes)
            res.append([account] + sorted(nodes))
        return res


class Solution2:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_idx = defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_to_idx[email].append(i)

        def dfs(i, nodes):
            visited[i] = True
            for email in accounts[i][1:]:
                if email in nodes:
                    continue
                nodes.append(email)
                for j in email_to_idx[email]:
                    if not visited[j]:
                        dfs(j, nodes)

        res = []
        visited = [False] * len(accounts)
        for i, b in enumerate(visited):
            if not b:
                nodes = []
                dfs(i, nodes)
                res.append([accounts[i][0]] + sorted(nodes))
        return res


# Union Find
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
        x_rank = self.rank[px]
        y_rank = self.rank[py]
        if x_rank < y_rank:
            self.parent[px] = py
        elif x_rank > y_rank:
            self.parent[py] = px
        else:
            self.parent[px] = py
            self.rank[py] += 1


class Solution3:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        email_to_idx = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in email_to_idx:
                    uf.union(i, email_to_idx[email])
                email_to_idx[email] = i
        res = defaultdict(list)
        for email, i in email_to_idx.items():
            res[uf.find(i)].append(email)
        return [[accounts[i][0]] + sorted(emails) for i, emails in res.items()]