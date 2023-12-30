class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacent = collections.defaultdict(list)
        indegree = [0] * numCourses

        for pre in prerequisites:
            adjacent[pre[1]].append(pre[0])
            indegree[pre[0]] += 1

        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        visited = 0
        while queue:
            node = queue.pop(0)
            visited += 1
            for adj in adjacent[node]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    queue.append(adj)

        return visited == numCourses