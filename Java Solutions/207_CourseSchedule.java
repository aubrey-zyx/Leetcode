class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adjacent = new ArrayList<>();
        int[] indegree = new int[numCourses];
        for (int i = 0; i < numCourses; i++) {
            adjacent.add(new ArrayList<>());
        }
        for (int[] pre : prerequisites) {
            adjacent.get(pre[1]).add(pre[0]);
            indegree[pre[0]]++;
        }

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                queue.offer(i);
            }
        }

        int visited = 0;
        while (!queue.isEmpty()) {
            int node = queue.poll();
            visited++;
            for (int adj : adjacent.get(node)) {
                indegree[adj]--;
                if (indegree[adj] == 0) {
                    queue.offer(adj);
                }
            }
        }

        return visited == numCourses;
    }
}