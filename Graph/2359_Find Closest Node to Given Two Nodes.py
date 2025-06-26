class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)

        def bfs(start, dist):
            queue = deque([start])
            visited = set([start])
            dist[start] = 0
            while queue:
                node = queue.popleft()
                nei = edges[node]
                if nei != -1 and nei not in visited:
                    dist[nei] = dist[node] + 1
                    queue.append(nei)
                    visited.add(nei)

        dist1, dist2 = [float("inf")] * n, [float("inf")] * n
        bfs(node1, dist1)
        bfs(node2, dist2)
        min_node, min_dist = -1, float("inf")
        for node in range(n):
            if max(dist1[node], dist2[node]) < min_dist:
                min_dist = max(dist1[node], dist2[node])
                min_node = node
        return min_node