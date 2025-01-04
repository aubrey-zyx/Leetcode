class Solution {
    public String reorganizeString(String s) {
        int[] cnt = new int[26];
        for (char c : s.toCharArray()) {
            if (++cnt[c - 'a'] > (s.length() + 1) / 2) {
                return "";
            }
        }

        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> Integer.compare(b[1], a[1]));
        for (int i = 0; i < 26; i++) {
            if (cnt[i] > 0) {
                heap.offer(new int[]{i + 'a', cnt[i]});
            }
        }

        StringBuilder sb = new StringBuilder();
        while (heap.size() > 1) {
            int[] first = heap.poll();
            int[] second = heap.poll();
            char c1 = (char) first[0];
            char c2 = (char) second[0];
            sb.append(c1);
            sb.append(c2);
            if (--first[1] > 0) {
                heap.offer(first);
            }
            if (--second[1] > 0) {
                heap.offer(second);
            }
        }
        if (!heap.isEmpty()) {
            sb.append((char) heap.poll()[0]);
        }

        return sb.toString();
    }
}


class Solution2 {
    public String reorganizeString(String s) {
        HashMap<Character, Integer> cnt = new HashMap<>();
        for (char c : s.toCharArray()) {
            int freq = cnt.getOrDefault(c, 0) + 1;
            if (freq > (s.length() + 1) / 2) return "";
            cnt.put(c, freq);
        }

        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> Integer.compare(b[1], a[1]));
        for (char c : cnt.keySet()) {
            heap.offer(new int[]{c, cnt.get(c)});
        }

        StringBuilder sb = new StringBuilder();
        while (heap.size() > 1) {
            int[] first = heap.poll();
            int[] second = heap.poll();
            char c1 = (char) first[0];
            char c2 = (char) second[0];
            sb.append(c1);
            sb.append(c2);
            if (--first[1] > 0) {
                heap.offer(first);
            }
            if (--second[1] > 0) {
                heap.offer(second);
            }
        }
        if (!heap.isEmpty()) {
            sb.append((char) heap.poll()[0]);
        }

        return sb.toString();
    }
}