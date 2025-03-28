class Solution {
    public String removeKdigits(String num, int k) {
        int n = num.length();
        if (k >= n) {
            return "0";
        }

        Stack<Character> stack = new Stack<>();

        for (char ch : num.toCharArray()) {
            while (k > 0 && !stack.isEmpty() && stack.peek() > ch) {
                stack.pop();
                k--;
            }
            stack.push(ch);
        }

        while (k > 0) {
            stack.pop();
            k--;
        }

        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }
        sb.reverse();
        while (sb.length() > 1 && sb.charAt(0) == '0') {
            sb.deleteCharAt(0);
        }

        return sb.toString();
    }
}