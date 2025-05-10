class Solution {
    private String s;
    private Set<String> wordSet;
    private List<String> res = new ArrayList<>();

    public List<String> wordBreak(String s, List<String> wordDict) {
        this.s = s;
        this.wordSet = new HashSet<>(wordDict);
        backtrack(0, new StringBuilder());
        return res;
    }

    private void backtrack(int start, StringBuilder curSentence) {
        if (start == s.length()) {
            res.add(curSentence.toString().trim());
            return;
        }

        for (int end = start + 1; end <= s.length(); end++) {
            String word = s.substring(start, end);
            if (wordSet.contains(word)) {
                int curLength = curSentence.length();
                curSentence.append(word).append(" ");
                backtrack(end, curSentence);
                curSentence.setLength(curLength);
            }
        }
    }
}