class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> heap = new PriorityQueue<>(
            (a, b) -> Integer.compare(b[0], a[0])
        );
        for (int i = 0; i < points.length; i++) {
            int[] entry = {squaredDistance(points[i]), i};
            if (heap.size() < k) {
                heap.offer(entry);
            } else if (entry[0] < heap.peek()[0]) {
                heap.poll();
                heap.offer(entry);
            }
        }

        int[][] res = new int[k][2];
        for (int i = 0; i < k; i++) {
            res[i] = points[heap.poll()[1]];
        }
        return res;
    }

    private int squaredDistance(int[] point) {
        return point[0] * point[0] + point[1] * point[1];
    }
}