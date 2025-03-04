class Solution {
    public int characterReplacement(String s, int k) {
        int[] count = new int[26];
        int l = 0, res = 0;
        int maxFreq = 0;

        for (int r = 0; r < s.length(); r++) {
            int rChar = s.charAt(r) - 'A';
            count[rChar] += 1;
            maxFreq = Math.max(maxFreq, count[rChar]);
            if (r - l + 1 - maxFreq > k) {
                int lChar = s.charAt(l) - 'A';
                count[lChar] -= 1;
                l += 1;
            }
            res = r - l + 1;
        }

        return res;
    }
}
