class Solution {
    private List<String> res = new ArrayList<>();
    private Map<Character, String> letters = Map.of(
        '2', "abc",
        '3', "def",
        '4', "ghi",
        '5', "jkl",
        '6', "mno",
        '7', "pqrs",
        '8', "tuv",
        '9', "wxyz"
    );
    private String phoneDigits;

    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0) {
            return res;
        }

        phoneDigits = digits;
        backtrack(0, new StringBuilder());
        return res;
    }

    private void backtrack(int i, StringBuilder path) {
        if (path.length() == phoneDigits.length()) {
            res.add(path.toString());
            return;
        }

        String options = letters.get(phoneDigits.charAt(i));
        for (char letter : options.toCharArray()) {
            path.append(letter);
            backtrack(i + 1, path);
            path.deleteCharAt(path.length() - 1);
        }
    }
}