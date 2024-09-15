class Solution {
    public int firstUniqChar(String s) {
        Map<Character, Integer> counter = new HashMap<>();
        for (char ch : s.toCharArray()) {
            counter.put(ch, counter.getOrDefault(ch, 0) + 1);
        }
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (counter.get(ch) == 1) {
                return i;
            }
        }
        return -1;
    }
}