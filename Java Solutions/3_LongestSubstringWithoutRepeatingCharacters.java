class Solution {
    public int lengthOfLongestSubstring(String s) {
        int l = 0, res = 0;
        Map<Character, Integer> pos = new HashMap<>();
        for (int r = 0; r < s.length(); r++) {
            char ch = s.charAt(r);
            if (pos.containsKey(ch) && pos.get(ch) >= l) {
                l = pos.get(ch) + 1;
            }
            pos.put(ch, r);
            res = Math.max(res, r - l + 1);
        }
        return res;
    }
}