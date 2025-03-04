class Solution {
    public boolean validTree(int n, int[][] edges) {
        List<List<Integer>> adjacent = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjacent.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            adjacent.get(edge[0]).add(edge[1]);
            adjacent.get(edge[1]).add(edge[0]);
        }
        
        Queue<Integer> queue = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();
        queue.offer(0);
        visited.add(0);
        Map<Integer, Integer> parent = new HashMap<>();

        while (!queue.isEmpty()) {
            int node = queue.poll();
            for (int nei : adjacent.get(node)) {
                if (parent.getOrDefault(node, -1) == nei) continue;
                if (visited.contains(nei)) return false;
                parent.put(nei, node);
                queue.offer(nei);
                visited.add(nei);
            }
        }
        return visited.size() == n;
    }
}
